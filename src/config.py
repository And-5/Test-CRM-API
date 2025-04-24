import os

API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL")
GET_CUSTOMERS = os.environ.get("GET_CUSTOMERS", "/api/customers")
CREATE_CUSTOMER = os.environ.get("CREATE_CUSTOMER", "/api/customers/create")
ORDERS_CUSTOMER = os.environ.get("ORDERS_CUSTOMER", "/api/customers/orders")
CREATE_ORDER = os.environ.get("CREATE_ORDER", "/api/orders/create")
PAYMENT_ORDER = os.environ.get("PAYMENT_ORDER", "/api/payments/create")
