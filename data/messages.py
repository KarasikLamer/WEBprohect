import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Message(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'messages'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String)
    ignore = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    important = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    sender_id = sqlalchemy.Column(sqlalchemy.Integer)
    receiver_id = sqlalchemy.Column(sqlalchemy.Integer)
