from flask import Flask, jsonify, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'via_post': some_json}), 201
    else:
        return jsonify({'via_get': 'Hello World!'})


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()