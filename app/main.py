
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(
    title="SEC-AGENCY",
    description="Secure Enterprise Order Management API",
    version="1.0.0"
)

orders = {}


class Order(BaseModel):
    customer_name: str
    description: str


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "sec-agency"
    }


@app.post("/orders", status_code=201)
def create_order(order: Order):
    order_id = str(uuid4())

    orders[order_id] = {
        "id": order_id,
        "customer_name": order.customer_name,
        "description": order.description,
        "status": "PENDING"
    }

    return orders[order_id]


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id not in orders:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return orders[order_id]


@app.get("/")
def root():
    return {"message": "SEC-AGENCY API online"}
