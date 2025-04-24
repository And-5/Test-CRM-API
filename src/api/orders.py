from fastapi import APIRouter
from typing import Optional
from services.api_client import ApiClient
from schemas.orders import CreateOrder

from config import ORDERS_CUSTOMER, CREATE_ORDER

from utils.build_request_url import build_request_url

router = APIRouter(tags=["Orders"])
api_client = ApiClient()


@router.get("")
def get_orders(customer_id: Optional[int]):
    params = {
        "customerId": customer_id
    }
    request_url = build_request_url(ORDERS_CUSTOMER, params)

    response = api_client.get(request_url)
    return response.json()


@router.post("/create")
def create_order(order: CreateOrder):
    order_data = {
        "number": order.number,
        "customer": {"id": order.customer_id},
        "items": [
            {
                "offer": {
                    "id": oid
                }
            }
            for oid in order.order_ids
        ]
    }

    response = api_client.post(CREATE_ORDER, order_data, key="order")
    return response.json()
