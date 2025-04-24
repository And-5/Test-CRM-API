from typing import Optional, List

from pydantic import BaseModel


class CreateOrder(BaseModel):
    number: Optional[str]
    customer_id: Optional[int]
    order_ids: Optional[List[int]]
