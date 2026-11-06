from fastapi import FastAPI, Query
from faker import Faker
import random

from datetime import date, datetime
from zoneinfo import ZoneInfo
from uuid import uuid4

from products import product_list, country_list



# Create FastAPI application
app = FastAPI()

Faker.seed(1234)
fake = Faker('en_US')



@app.get("/fake_customers")
def get_fake_customers(
            num: int = Query(default=1, ge=1, le=50)
    ):
    cust_to_return = []
    for i in range(num):
        cust_to_return.append(
            {
                "customer_id": fake.uuid4(),
                'name': fake.name(),
                'email': fake.email(),
                'state': fake.state(),
                'signup_date': fake.date_between(start_date= date(2026, 1, 1), end_date=date(2026, 6, 30)),
            }
        )
    return cust_to_return



@app.get("/fake_orders")
def get_fake_orders(
        num: int = Query(default=1, ge=1, le=50)
    ):
    ord_to_return = []

    order_items = []
    for i in range( random.randint(1,3) ):
        rand_prod = random.choice(product_list)
        order_items.append({
            "product_id": rand_prod["product_id"],
            "product_name": rand_prod["product_name"],
            "category": rand_prod["category"],
            "unit_price": rand_prod["unit_price"],
            "quantity": random.randint(1,10),
        })

    for i in range(num):
        ord_to_return.append({
            "event_id": uuid4(),
            "event_type": "order_created",
            "event_time": datetime.now(ZoneInfo("Asia/Taipei")),
            "order": {
                "order_id": uuid4(),
                "status": "paid",
                "currency": "usd",
                "customer": {
                    "customer_id" : uuid4(),
                    "name": fake.name(),
                    "email": fake.email(),
                    "country": random.choice(country_list),
                } ,
                "items": order_items
            }
        })
    return ord_to_return


@app.get("/fake_orders/product_list")
def get_fake_orders_product_list():
    return product_list

