from flask import Blueprint, render_template

team_pages = Blueprint("team_pages", __name__)

@team_pages.route("/teams")
def teams_pages():
    return render_template("team_list.html")

@team_pages.route("/teams/<tag>")
def one_team_page(tag):
    return render_template("one_team.html")

@team_pages.route("/teams/<tag>/<char_id>")
def character_page(tag, char_id):
    return ""