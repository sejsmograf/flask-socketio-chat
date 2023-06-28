# Flask Chat Application
This is a simple chat application built with Python Flask, Flask-SocketIO, Flask-SQLAlchemy, Flask-Login, Bootstrap. It was rushed in few days for university project. The chat application allows multiple users to join chat rooms and exchange real-time messages with each other. It uses WebSocket communication through Socket.IO for real-time messaging and Flask-Login for user authentication. The application also utilizes Flask-SQLAlchemy to store user information and chat history in sqlite database.

## Features
- Real time messaging through SocketIO
- User authenthication and session management with Flask-Login
- Creating and joining chat rooms
- Chat history persistance
- Responsive design using Bootstrap

## Installation
- (Recommended) Create virtual python envirionment and activate it
```
python -m venv env
source env/bin/activate
```
- Install the dependencies from requirements.txt file
```
pip install -r requirements.txt
```
- Run the server
```
flask run
```
- You should be able to access the site on localhost:5000
