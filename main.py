from data import db_session
from data.users import Login
from data.messages import Message
from data.receiver_messages import ReceiverMessages
from data.sender_messages import SenderMessages


def main():
    db_session.global_init("db/projectWEB.sqlite")


if __name__ == '__main__':
    main()
