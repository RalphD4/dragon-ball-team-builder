from flask import Blueprint

#edit team
edit_team_route = Blueprint("edit_team_route", __name__)
@edit_team_route.route("/teams/<tag>/edit")
def edit_team():
    return 