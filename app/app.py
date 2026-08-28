from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/admin")
def admin():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    with open("../logs/access.log", "a") as log:
        log.write(f"{timestamp} | IP: {ip} | Endpoint: /admin\n")
    return "Admin panel -Authorized users only"
@app.route("/backup/employee_credentials.txt")
def credentials_decoys():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    with open("../logs/access.log", "a") as log:
       log.write(f"{timestamp} | IP: {ip} | DECOY: employee_credentials.txt\n")
    with open("../decoys/employee_credentials.txt", "r") as file:
       return "<pre>" + file.read() + "</pre>;"
@app.errorhandler(404)
def page_not_found(error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    path = request.path
    with open("../logs/access.log", "a") as log:
        log.write(f"{timestamp} | IP: {ip} | 404 PRONE: {path}\n")
    return "404 Not Found", 404
@app.route("/api/v1/users")
def fake_users_api():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr

    with open("../logs/access.log", "a") as log:
        log.write(f"{timestamp} | IP: {ip} | DECOY API: /api/v1/users\n")

    return {
        "status": "success",
        "users": [
            {"username": "admin", "role": "administrator"},
            {"username": "backup", "role": "system"}
        ]
    }
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
