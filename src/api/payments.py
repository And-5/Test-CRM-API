from fastapi import APIRouter

from services.api_client import ApiClient
from schemas.payments import PaymentOrder

from config import PAYMENT_ORDER

router = APIRouter(tags=["Payments"])
api_client = ApiClient()


@router.post("/create")
def create_payment_order(payment_order: PaymentOrder):
    payment_data = {
        "order": {"id": payment_order.order_id},
        "amount": payment_order.amount,
        "comment": payment_order.comment,
        "type": payment_order.type
    }

    response = api_client.post(PAYMENT_ORDER, payment_data, key="payment")
    return response.json()
