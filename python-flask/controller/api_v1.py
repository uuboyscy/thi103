from flask import Blueprint

api_v1 = Blueprint("api_v1", __name__)

@api_v1.route("/do_nothing")
def do_nothing():
    return "<h1>Do noyhing.</h1>"
