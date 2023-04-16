from flask_restful import Resource, reqparse, abort
from data import db_session
from data.messages import Message
from flask import jsonify
from sqlalchemy.exc import IntegrityError


class MessageResource(Resource):
    @staticmethod
    def get(id_message):
        db_sess = db_session.create_session()
        message = db_sess.query(Message).get(id_message)
        if not message:
            abort(404, message=f'Message {id_message} not Found')
        return jsonify({"messages": message.to_dict(
            only=('id', 'ignore', 'important', 'show_message', 'receiver_id', 'sender_id', 'content')
        )})

    @staticmethod
    def delete(id_message):
        db_sess = db_session.create_session()
        message = db_sess.query(Message).get(id_message)
        if not message:
            abort(404, message=f'Message {id_message} not Found')
        db_sess.delete(message)
        db_sess.commit()
        return jsonify({"success": 'OK'})


class MessageListResource(Resource):
    @staticmethod
    def get():
        pass

    @staticmethod
    def post():
        pass
