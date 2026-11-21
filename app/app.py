import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Hello tu container: {socket.gethostname()}</h1>\n"

@app.route("/health")
def health():
    return {"status": "ok"}
