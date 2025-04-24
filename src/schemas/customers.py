from typing import Optional

from pydantic import BaseModel


class CreateCustomer(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    mobile: Optional[str] = None
