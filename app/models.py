from pydantic import BaseModel

class Order(BaseModel):
    client_id: str
    quantity: int
