import os
import sqlite3
import re
import shlex
from flask import Flask, request
from subprocess import run, PIPE

app = Flask(__name__)

@app.route("/users")
def get_user():
    name = request.args.get("name", "")
    if not isinstance(name, str) or not re.match(r'^[\w\s]{1,100}$', name):
        return {"error": "Invalid input"}, 400
    conn = sqlite3.connect("test.db")
    cursor = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    return str(cursor.fetchall())

@app.route("/exec")
def run_command():
    cmd = request.args.get("cmd", "")
    if not isinstance(cmd, str) or len(cmd) > 200:
        return {"error": "Invalid command"}, 400
    args = shlex.split(cmd)
    result = run(args, capture_output=True, text=True, timeout=5)
    return result.stdout

if __name__ == "__main__":
    app.run(debug=False)
