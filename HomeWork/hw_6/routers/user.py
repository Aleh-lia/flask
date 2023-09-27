from fastapi import APIRouter
from db import users, database
from models.user import User

router = APIRouter()


@router.post("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(lastname=f'last_{i}',
                                      firstname=f'first_{i}',
                                      email=f'user{i}@example.com',
                                      password=f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users created'}


@router.get("/users", response_model=list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@router.post("/users", response_model=User)
async def create_user(user: User):
    query = users.insert().values(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=user.password
    )
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: User):
    query = users.update().where(users.c.id ==
                                 user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


