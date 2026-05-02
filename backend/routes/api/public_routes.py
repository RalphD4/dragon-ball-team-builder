from flask import jsonify, Blueprint
from backend.data.database import TEAM_TAGS
from backend.services.team_service import TEAMS

#Teams, Team, Character


#One blue print for Teams -> Team -> Character
team_api = Blueprint("api", __name__, url_prefix="/api")

# ------------------    character route
@team_api.route("/teams/<tag>/<char_id>")
def get_character(tag, char_id):

    tag = tag.replace("-", " ").lower()

    enum_tag = next(
        (t for t in TEAM_TAGS if t.value.lower() == tag.lower()),
        None
    )
    if not enum_tag:
        return {"error": "Invalid team"}, 404
    team = TEAMS.get(enum_tag)
    if not team:
        return {"error": "Team not found"}, 404
    

    #Find character inside team
    character = next(
        (char for char in team.characters if char.char_id == char_id),
        None
    )
    if not character:
        return {"error": "Character not found in this team"}, 404 

    return jsonify(character.to_dict())




# ----------------  1 team route 
@team_api.route("/teams/<tag>", methods=["GET"])
def get_team(tag):

    tag = tag.replace("-", " ").lower()

    enum_tag = next(
        (t for t in TEAM_TAGS if t.value.lower() == tag.lower()),
        None
    )

    if not enum_tag:
        return {"error": "Invalid team"}, 404

    team = TEAMS.get(enum_tag)

    if not team:
        return {"error": "Team not found"}, 404

    return jsonify(team.to_dict())



# -------- team list route
@team_api.route("/teams", methods=["GET"])
def get_teams():
    #team names sorted alphatically
    sorted_teams = sorted(TEAMS.values(), key=lambda e: e.name)
    return jsonify([
    {
        "name": team.tag.value,  # display name
        "tag": team.tag.value.replace(" ", "-").lower()  # URL slug
    }
    for team in sorted_teams
])
