from typing import Optional

from pydantic import BaseModel


class PaymentOrder(BaseModel):
    order_id: Optional[int]
    amount: Optional[float]
    comment: Optional[str]
    type: Optional[str]
