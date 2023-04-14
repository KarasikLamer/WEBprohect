import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class ReceiverMessages(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "receivers_to_messages"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    receiver_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    message_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("messages.receiver_id"))
