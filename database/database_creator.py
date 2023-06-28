from . import db
from flask_login import UserMixin


user_room = db.Table(
    "user_in_rooms",
    db.Column("room_id", db.Integer, db.ForeignKey("rooms.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
)


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True, nullable=False)
    email = db.Column(db.String(55), unique=True, nullable=False)
    password = db.Column(db.String(255))
    messages = db.relationship("Message", backref="user")

    rooms = db.relationship("Room", secondary=user_room, backref="users")

    def __repr__(self):
        return f"<User {self.username}>"


class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_code = db.Column(db.String(55), unique=True, nullable=False)


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=False)
    send_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    room_code = db.Column(db.String, db.ForeignKey("rooms.room_code"))
