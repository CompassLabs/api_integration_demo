from decimal import Decimal
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from compass.api_client.models.token import Token

# generic types for compass API

T = TypeVar("T")


class BaseTransactionRequest(BaseModel, Generic[T]):
    sender: str
    call_data: T


class FunctionCallData(BaseModel):
    pass


# specific models for this integration


class GetErc20Balance(BaseModel):
    user: str = Field(
        ...,
        description="The user to get the ERC20 balance of.",
        examples=["0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"],
    )
    token: Token = Field(
        ...,
        description="The symbol of the token for which the allowance is checked.",
        examples=[Token.WETH],
    )


class WrapEthRequestCallData(FunctionCallData):
    # the arguments for any on-chain requests you need to create an unsigned transaction, and the arguments for the the transaction itself
    amount: Decimal = Field(
        ...,
        description="The amount of ETH to wrap.",
        examples=[1.5],
    )


class WrapEthRequest(BaseTransactionRequest[WrapEthRequestCallData]):
    # we must encapsulate request models that intend to return an unsigned transaction in BaseTransactionRequest
    pass
