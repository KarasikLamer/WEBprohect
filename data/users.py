import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    phone = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    second_email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)

    received_messages = orm.relationship("Message", back_populates="receiver")
    sent_messages = orm.relationship("Message", back_populates="sender")

    admin = orm.relationship("Admin", back_populates="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_phone(self, phone):
        self.phone = phone

    def set_second_email(self, email):
        self.second_email = email
