import datetime
from data import db_session
from data.users import User
from data.messages import Message
from data.admins import Admin
from flask_restful import Api
from flask import Flask
import api_user
import api_message


app = Flask(__name__)
app.config['SECRET_KEY'] = 'VALERA_GO_SEX'
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=365 * 200)
api = Api(app)


def main():
    db_session.global_init("db/projectWEB3.sqlite")
    api.add_resource(api_user.UserResource, '/api/users/<int:user_id>')
    api.add_resource(api_user.UserListResource, '/api/users')
    api.add_resource(api_message.MessageResource, '/api/messages/<int:message_id>')
    api.add_resource(api_message.MessageListResource, '/api/messages')
    app.run()


if __name__ == '__main__':
    main()
