import os
import sqlite3
from flask import Flask, request
from subprocess import run, PIPE

app = Flask(__name__)

@app.route("/users")
def get_user():
    name = request.args.get("name", "")
    conn = sqlite3.connect("test.db")
    cursor = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    return str(cursor.fetchall())

@app.route("/exec")
def run_command():
    cmd = request.args.get("cmd", "")
    result = run(cmd, shell=True, capture_output=True, text=True, timeout=5)
    return result.stdout

if __name__ == "__main__":
    app.run(debug=False)
