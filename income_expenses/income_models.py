from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal
from datetime import date


class BaseIncome(BaseModel):
    income_id: int = Field(
        ...,
        description="Unique identifier for the income source.",
    )
    source: str
    frequency: Literal["hourly", "weekly", "biweekly", "monthly", "yearly"]
    amount_dollars: int
    amount_cents: Optional[int] = None


class HourlyIncome(BaseIncome):
    hours_per_week: int = Field(
        ...,
        description="Number of hours worked per week.",
    )

    @field_validator("hours_per_week", mode="before")
    def validate_hours_per_week(cls, v):
        if v < 0:
            raise ValueError("Hours per week must be a non-negative integer.")
        return v


class WeeklyIncome(BaseIncome):
    day_of_week: int = Field(
        ...,
        description="Day of the week when the income is received, represented as an integer (1-7, where 1 is Sunday).",
    )

    @field_validator("day_of_week", mode="before")
    def validate_day_of_week(cls, v):
        if not (1 <= v <= 7):
            raise ValueError("Day of the week must be between 1 and 7.")
        return v


class BiweeklyIncome(BaseIncome):
    last_payment_date: date = Field(
        ...,
        description="Date of the last payment received.",
    )

    @field_validator("last_payment_date", mode="before")
    def validate_last_payment_date(cls, v):
        if not isinstance(v, date):
            raise ValueError("Last payment date must be a valid date object.")
        return v


class MonthlyIncome(BaseIncome):
    due_date: int = Field(
        ...,
        description="Due date of the income, represented as an integer (1-31).",
    )

    @field_validator("due_date", mode="before")
    def validate_due_date(cls, v):
        if not (1 <= v <= 31):
            raise ValueError("Due date must be between 1 and 31.")
        return v


class YearlyIncome(BaseIncome):
    month: int = Field(
        ...,
        description="Month of the year when the income is received, represented as an integer (1-12).",
    )
    day: int = Field(
        ...,
        description="Day of the month when the income is received, represented as an integer (1-31).",
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
