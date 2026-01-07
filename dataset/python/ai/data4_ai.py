from __future__ import annotations

from flask import Flask, jsonify, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handle GET and POST requests for the root endpoint.
    """
    if request.method == "POST":
        payload = request.get_json()
        return jsonify(via_post=payload), 201

    return jsonify(via_get="Hello World!")


def run_production_server(
    host: str = "127.0.0.1",
    port: int = 5000,
) -> None:
    """
    Run the application using a production-ready WSGI server.
    """
    server = WSGIServer((host, port), app)
    server.serve_forever()


def main() -> None:
    run_production_server()


if __name__ == "__main__":
    main()
