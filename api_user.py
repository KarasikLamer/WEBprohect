from flask_restful import Resource, abort, reqparse
from data import db_session
from data.users import User
from flask import jsonify
from sqlalchemy.exc import IntegrityError


parser = reqparse.RequestParser()
parser.add_argument("name", location="args", required=True)
parser.add_argument('cn', location='args', default=False, type=bool)  # change name
parser.add_argument("surname", location="args", required=True)
parser.add_argument('cs', location='args', default=False, type=bool)  # change surname
parser.add_argument("password", location="args", required=True)
parser.add_argument('cp', location='args', default=False, type=bool)  # change password
parser.add_argument("email", location='args', required=True)
parser.add_argument('ce', localion='args', default=False, type=bool)  # change email
parser.add_argument('second_email', location='args')
parser.add_argument('cse', localion='args', default=False, type=bool)  # change second email
parser.add_argument("phone", location="args")
parser.add_argument('cpn', localion='args', default=False, type=bool)  # change phone number


class UserResource(Resource):
    @staticmethod
    def get(id_user):
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(id_user)
        if not user:
            abort(404, message=f'User {id_user} not Found')
        return jsonify({"users": user.to_dict(only=("id", "name", "surname", "email"))})

    @staticmethod
    def delete(id_user):
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(id_user)
        if not user:
            abort(404, message=f'User {id_user} not Found')
        db_sess.delete(user)
        return jsonify({"success": "OK"})

    @staticmethod
    def put(id_user):
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(id_user)
        if not user:
            abort(404, message=f'User {id_user} not Found')
        args = parser.parse_args()
        user.name = args['name'] if args['cn'] else user.name
        user.surname = args['surname'] if args['cs'] else user.surname
        user.email = args['email'] if args['ce'] else user.email
        user.second_email = args['second_email'] if args['cse'] else user.second.email
        user.phone = args['phone'] if args['cpn'] else user.phone
        if args['cp']:
            user.set_password(args['password'])
        try:
            db_sess.commit()
            return jsonify({"success": "OK"})
        except IntegrityError as er:
            abort(409, message=str(er))


class UserListResource(Resource):
    @staticmethod
    def get():
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify({"users": [
            item.to_dict(only=('id', 'name', 'surname', 'email')) for item in users
        ]})

    @staticmethod
    def post():
        args = parser.parse_args()
        user = User()
        user.name = args['name']
        user.surname = args['surname']
        user.email = args['email']
        if args['second_email']:
            user.second_email = args['second_email']
        if args['phone']:
            user.phone = args['phone']
        user.set_password(args['password'])
        db_sess = db_session.create_session()
        try:
            db_sess.add(user)
            db_sess.commit()
            return jsonify({"success": "OK"})
        except IntegrityError as er:
            abort(409, message=str(er))
