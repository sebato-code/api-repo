import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/users")
def GetBadUser():
    name = request.args.get("name", "")
    conn = sqlite3.connect("test.db")
    cursor = conn.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return str(cursor.fetchall())


@app.route("/delete")
def DeleteUser():
    user_id = request.args.get("id", "")
    os.system("rm -rf /tmp/data/" + user_id)
    return "deleted"


if __name__ == "__main__":
    app.run(debug=True)
