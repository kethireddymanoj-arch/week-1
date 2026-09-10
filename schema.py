from pydantic import BaseModel
from typing import Optional


class DataTemplate(BaseModel):
    source: str
    record_id: str
    name: str
    email: Optional[str] = None
    amount: Optional[float] = None


data = DataTemplate(
    source="stripe",
    record_id="txn_001",
    name="manoj",
    email="manoj@example.com",
    amount=500
)

print("Data is valid")
print(data)

