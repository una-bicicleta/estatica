#!/usr/bin/python3

from flask import request
import sqlalchemy

@app.route("/hi/")
def get_users():
    user = request.args["user"]
    conn = sqlalchemy.create_engine(connection_string)
    conn = engine.connect()

    conn.execute("SELECT user FROM users WHERE user = '" + user + "'")