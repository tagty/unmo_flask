from flask import Flask, render_template
from flask_socketio import SocketIO, send
import sys
from unmo import Unmo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello():
    return render_template('hello.html')

def build_prompt(unmo):
    return '{name}:{responder}> '.format(name=unmo.name, responder=unmo.responder_name)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message, file=sys.stderr)
    send(message, broadcast=True)

    proto = Unmo('proto')

    try:
        response = proto.dialogue(message)
    except IndexError as error:
        print('{}: {}'.format(type(error).__name__, str(error)))
        print('Error: Dictionary is empty. (Responder: {})'.format(proto.responder_name))
    else:
        print('{prompt}{response}'.format(prompt=build_prompt(proto), response=response))

    print('response message: ' + response, file=sys.stderr)
    prompt_response = '{prompt}{response}'.format(prompt=build_prompt(proto), response=response)
    send(prompt_response, broadcast=True)

    proto.save()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)

