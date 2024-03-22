from typing import List

from pydantic import BaseModel


class Product(BaseModel):
    product_name: str
    price: float
    quantity: int


class Order(BaseModel):
    user_id: str
    total_price: float
    products: List[Product]

