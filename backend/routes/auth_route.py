from flask import Blueprint, jsonify


login_route = Blueprint("login_route", __name__)
@login_route.route("/login")
def login_page():
    return jsonify({"message": "Login page"})