import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.controllers import UserController, TransactionController


def new_session_factory():
    load_dotenv()

    db_host = os.getenv("DB_HOST", "")
    db_port = os.getenv("DB_PORT", "")
    db_schema = os.getenv("DB_SCHEMA", "")
    db_user = os.getenv("DB_USER", "")
    db_password = os.getenv("DB_PASSWORD", "")

    uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_schema}"

    return sessionmaker(bind=create_engine(uri))


session_factory = new_session_factory()
db_session = session_factory()

user_controller = UserController(db_session)
transaction_controller = TransactionController(db_session)
