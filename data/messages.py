import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Message(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'messages'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String)
    ignore = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    important = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    show_message = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    receiver_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    sender_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))

    receiver = orm.relationship("User", back_populates="received_messages")
    sender = orm.relationship("User", back_populates="sent_messages")
