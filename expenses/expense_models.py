from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal, Union
from datetime import date


class BaseBill(BaseModel):
    expense_id: int = Field(
        ...,
        description="Unique identifier for the bill.",
    )
    name: str
    amount_dollars: int
    amount_cents: Optional[int] = None
    frequency: Literal["monthly", "yearly", "weekly", "biweekly"] = "monthly"


class MonthlyBill(BaseBill):
    due_date: int = Field(
        ...,
        description="Due date of the bill, represented as an integer (1-31).",
    )

    @field_validator("due_date", mode="before")
    def validate_due_date(cls, v):
        if not (1 <= v <= 31):
            raise ValueError("Due date must be between 1 and 31.")
        return v


class AnnualBill(BaseBill):
    month: int = Field(
        ...,
        description="Month of the year when the bill is due, represented as an integer (1-12).",
    )
    day: int = Field(
        ...,
        description="Day of the month when the bill is due, represented as an integer (1-31).",
    )

    @field_validator("day", mode="before")
    def validate_day(cls, v):
        if not (1 <= v <= 31):
            raise ValueError("Day must be between 1 and 31.")
        return v

    @field_validator("month", mode="before")
    def validate_month(cls, v):
        if not (1 <= v <= 12):
            raise ValueError("Month must be between 1 and 12.")
        return v


class WeeklyBill(BaseBill):
    day_of_week: int = Field(
        ...,
        description="Day of the week when the bill is due, represented as an integer (1-7, where 1 is Sunday).",
    )

    @field_validator("day_of_week", mode="before")
    def validate_day_of_week(cls, v):
        if not (1 <= v <= 7):
            raise ValueError("Day of the week must be between 1 and 7.")
        return v


class BiweeklyBill(BaseBill):
    last_known_due_date: date = Field(
        ...,
        description="Last known due date of the bill, represented as a date object.",
    )

    @field_validator("last_known_due_date", mode="before")
    def validate_last_known_due_date(cls, v):
        if not isinstance(v, date):
            raise ValueError("Last known due date must be a date object.")
        return v
