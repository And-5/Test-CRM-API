from fastapi import FastAPI

from api import customers, orders, payments

app = FastAPI()

app.include_router(customers.router, prefix="/customers")
app.include_router(orders.router, prefix="/orders")
app.include_router(payments.router, prefix="/payments")
