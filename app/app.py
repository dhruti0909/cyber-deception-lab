from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "logs", "access.log")
DECOY_FILE = os.path.join(BASE_DIR, "decoys", "employee_credentials.txt")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/admin")
def admin():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr

    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} | IP: {ip} | Endpoint: /admin\n")

    return "Admin panel -Authorized users only"


@app.route("/backup/employee_credentials.txt")
def credentials_decoys():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr

    with open(LOG_FILE, "a") as log:
        log.write(
            f"{timestamp} | IP: {ip} | DECOY: employee_credentials.txt\n"
        )

    with open(DECOY_FILE, "r") as file:
        return "<pre>" + file.read() + "</pre>"


@app.errorhandler(404)
def page_not_found(error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    path = request.path

    with open(LOG_FILE, "a") as log:
        log.write(
            f"{timestamp} | IP: {ip} | 404 PRONE: {path}\n"
        )

    return "404 Not Found", 404


@app.route("/api/v1/users")
def fake_users_api():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr

    with open(LOG_FILE, "a") as log:
        log.write(
            f"{timestamp} | IP: {ip} | DECOY API: /api/v1/users\n"
        )

    return {
        "status": "success",
        "users": [
            {"username": "admin", "role": "administrator"},
            {"username": "backup", "role": "system"}
        ]
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
