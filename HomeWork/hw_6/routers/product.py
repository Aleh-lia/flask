from fastapi import APIRouter
from db import database, products
from models.product import Product

router = APIRouter()


@router.post("/fake_products/{count}")
async def create_note(count: int):
    for i in range(count):
        query = products.insert().values(name=f'name_{i}',
                                      description=f'product_{i}',
                                      price=f'{i}{i}{i}')
        await database.execute(query)
    return {'message': f'{count} fake orders created'}


@router.get("/products", response_model=list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.post("/products", response_model=Product)
async def create_product(product: Product):
    query = products.insert().values(
        name=product.name,
        description=product.description,
        price=product.price,
    )
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: Product):
    query =products.update().where(products.c.id ==
                                 product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'User deleted'}

