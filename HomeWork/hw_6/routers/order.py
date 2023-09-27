from fastapi import APIRouter
from db import database, orders
from models.order import Order

router = APIRouter()


@router.post("/fake_orders/{count}")
async def create_note(count: int):
    for i in range(count):
        query = orders.insert().values(user_id=f'{i}',
                                      product_id=f'{i}',
                                      order_date=f'{i+1}.09.2023',
                                      status=f'')
        await database.execute(query)
    return {'message': f'{count} fake orders created'}


@router.get("/orders", response_model=list[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.post("/orders", response_model=Order)
async def create_order(order: Order):
    query = orders.insert().values(
        user_id=order.user_id,
        product_id=order.product_id,
        order_date=order.order_date,
    )
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@router.get("/orders/{orders_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.put("/orders/{orders_id}", response_model=Order)
async def update_order(order_id: int, new_order: Order):
    query = orders.update().where(orders.c.id ==
                                 order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'User deleted'}

