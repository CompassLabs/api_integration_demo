from decimal import Decimal

from pydantic import BaseModel, Field

from compass.api_client.models.token import Token


class UnsignedTransaction(BaseModel):
    chainId: int = Field(..., description="The chain id of the transaction")
    data: str = Field(..., description="The data of the transaction")
    from_: str = Field(..., alias="from", description="The sender of the transaction")
    gas: int = Field(..., description="The gas of the transaction")
    to: str = Field(..., description="The recipient of the transaction")
    value: int = Field(..., description="The value of the transaction")
    nonce: int = Field(..., description="The nonce of the address")
    maxFeePerGas: int = Field(..., description="The max fee per gas of the transaction")
    maxPriorityFeePerGas: int = Field(
        ..., description="The max priority fee per gas of the transaction"
    )


class BalanceInfo(BaseModel):
    amount: Decimal = Field(
        ...,
        description="Amount of tokens a particular address holds",
        examples=[1.5],
    )
    decimals: int = Field(
        ..., description="Number of decimals of the token", examples=[18]
    )
    token_symbol: Token = Field(..., description="Symbol of the token")
    token_address: str = Field(
        ...,
        description="Address of the token",
        examples=["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
    )
