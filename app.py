from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    return render_template('hello.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)
