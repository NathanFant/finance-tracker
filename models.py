from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal, Union
from datetime import date, datetime
from tools import parse_due_date


class Income(BaseModel):
    source: str
    amount: float


class Bill(BaseModel):
    name: str
    amount: float
    due_date: Union[str, int, date, datetime] = Field(
        ...,
        description="Due date of the bill, can be a string in 'MM-DD-YYYY' format, an integer (1-31), or a date/datetime object.",
    )

    @field_validator("due_date", mode="before")
    def validate_due_date(cls, v):
        return parse_due_date(v)


class Loan(BaseModel):
    lender: str
    initial_amount: float
    interest_rate: float
    initial_date: date
    minimum_payment: float
    payments: List[float] = Field(default_factory=list)
    due_date: Optional[date] = None


class CreditCard(BaseModel):
    card_name: str
    balance: float
    interest_rate: float
    due_date: Optional[date] = None
    minimum_payment: Optional[float] = None


class SavingsGoal(BaseModel):
    amount: float
    interest_rate: float


class FinancialProfile(BaseModel):
    income: List[Income]
    bills: List[Bill]
    loans: List[Loan]
    credit_cards: List[CreditCard]
    savings_goals: List[SavingsGoal]
