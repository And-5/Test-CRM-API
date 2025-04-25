from fastapi import APIRouter
from typing import Optional
from pydantic import EmailStr

from services.api_client import ApiClient
from schemas.customers import CreateCustomer

from config import GET_CUSTOMERS, CREATE_CUSTOMER

from utils.validate_date import validate_date

from utils.build_request_url import build_request_url

router = APIRouter(tags=["Customers"])
api_client = ApiClient()


@router.get("")
def get_customers(name: Optional[str] = None,
                  email: Optional[EmailStr] = None,
                  create_date: Optional[str] = None):

    params = {
        "name": name,
        "email": email,
        "dateFrom": validate_date(create_date).date() if create_date else None,
        "dateTo": validate_date(create_date).date() if create_date else None
    }

    request_url = build_request_url(GET_CUSTOMERS, params)

    response = api_client.get(request_url)

    return response.json()


@router.post("/create")
def create_customer(customer: CreateCustomer):
    customer_data = {
        "firstName": customer.first_name,
        "lastName": customer.last_name,
        "email": customer.email,
        "phones": [
            {"number": customer.mobile}
        ]
    }

    response = api_client.post(CREATE_CUSTOMER, customer_data, key="customer")

    return response.json()
