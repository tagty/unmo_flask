from flask import Flask
from flask import render_template
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    #redis.incr('hits')
    #return 'Hello World! I have been seen %s times.' % redis.get('hits')
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
