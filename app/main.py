from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Set
from collections import deque
import asyncio
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class Order(BaseModel):
    client_id: str
    quantity: int


orders = deque()  
valid_client_ids: Set[str] = set()  
baristas = 10
clients_per_group = 150
brewing_time = 45 
delusional_ddoser_ip = "192.168.1.100"
order_lock = asyncio.Lock()

@app.post("/order/")
async def place_order(order: Order):
    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")
    
    async with order_lock:
        orders.append(order)
        valid_client_ids.add(order.client_id)

    return {"message": f"Order received for {order.quantity} americano(s)"}

@app.get("/start/")
async def start_preparing_orders():
    async with order_lock:
        if len(orders) == 0:
            return {"message": "No orders to prepare"}

        orders_to_prepare = []
        for _ in range(min(baristas, len(orders))):
            orders_to_prepare.append(orders.popleft())

    return {"message": "Started preparing orders", "orders": orders_to_prepare}

@app.post("/finish/")
async def finish_preparing_orders(finished_orders: List[Order]):
    errors = []
    for order in finished_orders:
        if order.client_id in valid_client_ids:
            print(f"Order for client {order.client_id} is ready")
            valid_client_ids.remove(order.client_id)
        else:
            errors.append(f"No order found for client {order.client_id}")

    if errors:
        raise HTTPException(status_code=400, detail="; ".join(errors))

    return {"message": "Orders finished"}

class DDoSProtectionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.client.host == delusional_ddoser_ip:
            raise HTTPException(status_code=429, detail="Too Many Requests")
        
        response = await call_next(request)
        return response

app.add_middleware(DDoSProtectionMiddleware)

async def brew_coffee(quantity):
    await asyncio.sleep(brewing_time * quantity)

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
