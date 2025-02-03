import json
import os

import devtools
from demo_integration.ERC20_integration.request import *
from demo_integration.ERC20_integration.response import *
from dotenv import load_dotenv
from web3 import HTTPProvider, Web3
from web3.contract import Contract

from compass.api_client.models.chain import Chain
from compass.api_client.models.token import Token

load_dotenv()
ETHEREUM_RPC_URL = os.getenv("ETHEREUM_RPC_URL")

w3 = Web3(HTTPProvider(ETHEREUM_RPC_URL))


def _read_contract_abi_file(file_path: str) -> dict[str, Any]:
    with open(os.path.join(os.path.dirname(__file__), f"{file_path}.json")) as file:
        return json.load(file)


def get_erc20_contract(address: str, abi_name: str) -> Contract:
    return w3.eth.contract(
        address=address, abi=_read_contract_abi_file(file_path=abi_name)
    )


def get_token_address(chain: Chain, token: Token) -> str:
    # you can assume that any tokens already in our API can have their addresses looked up
    # if you add new contracts though, you will have to supply config for their addresses on all chains!
    match chain:
        case Chain.ETHEREUM_COLON_MAINNET:
            match token:
                case Token.WETH:
                    address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
                case _:
                    raise Exception("Unsupported token!")
        case _:
            raise Exception("Unsupported chain!")
    return address


def get_erc20_balance_handler(
    chain: Chain, request_model: GetErc20Balance
) -> BalanceInfo:
    user, token = request_model.user, request_model.token
    address = get_token_address(chain, token)

    contract = get_erc20_contract(address, "ERC20")
    amount_in_wei = contract.functions.balanceOf(user).call()
    decimals = contract.functions.decimals().call()
    # it is important to return a human-readable value!
    return Decimal(str(amount_in_wei)) / Decimal(10**decimals)


def wrap_eth_handler(
    chain: Chain, request_model: WrapEthRequest
) -> UnsignedTransaction:
    sender, amount = request_model.sender, request_model.call_data.amount
    address = get_token_address(chain, Token.WETH)

    contract = get_erc20_contract(address, "WETH")
    unsigned_transaction = contract.functions.deposit().build_transaction(
        {
            "from": sender,
            "value": int(
                amount
            ),  # this would be incorrect as it is not adjusted for decimals!
            "nonce": 100,  # we can derive the nonce, you do not need to re-implement this
        }
    )
    return UnsignedTransaction(**unsigned_transaction)


# and then demonstrate usage/add tests
balance = get_erc20_balance_handler(
    Chain.ETHEREUM_COLON_MAINNET,
    GetErc20Balance(
        user="0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43", token=Token.WETH
    ),
)
wrap_eth_transaction = wrap_eth_handler(
    Chain.ETHEREUM_COLON_MAINNET,
    WrapEthRequest(
        sender="0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43",
        call_data=WrapEthRequestCallData(amount=0.001),
    ),
)

devtools.debug(balance)
devtools.debug(wrap_eth_transaction)
