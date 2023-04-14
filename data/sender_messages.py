import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class SenderMessages(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "senders_to_messages"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    sender_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    message_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("messages.sender_id"))
