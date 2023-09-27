import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
import databases as databases
from settings import settings


DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer,ForeignKey("users.id")),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, ForeignKey("products.id")),
    sqlalchemy.Column("order_date", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
)


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(32)),
    sqlalchemy.Column("lastname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
