from sqlalchemy import func
from sqlalchemy.orm import session

from app import models
from app.exceptions import UserNotFoundException, UserAlreadyExistsException


class UserController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def search_user(self, params: dict) -> dict:
        user = self.db_session.query(models.User).filter_by(**params).first()
        if not user:
            raise UserNotFoundException(params)

        income = self.db_session.query(func.sum(models.Transaction.amount)).filter_by(receiver=user.id_user).scalar()
        income = income if income else 0

        outcome = self.db_session.query(func.sum(models.Transaction.amount)).filter_by(sender=user.id_user).scalar()
        outcome = outcome if outcome else 0

        user_dict = user.to_dict()
        user_dict["balance"] = float(income - outcome)

        return user_dict

    def create_user(self, user: models.User) -> dict:
        if self.db_session.query(models.User).filter_by(username=user.username).first():
            raise UserAlreadyExistsException(user.username)

        self.db_session.add(user)
        self.db_session.commit()

        return user.to_dict()
