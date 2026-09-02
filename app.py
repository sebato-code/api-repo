import sqlite3
import re
from flask import Flask, request

app = Flask(__name__)

@app.route("/users")
def get_user():
    name = request.args.get("name", "")
    if not isinstance(name, str) or not re.match(r'^[\w\s]{1,100}$', name):
        return {"error": "Invalid input"}, 400
    conn = sqlite3.connect("test.db")
    cursor = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    return str(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=False)
