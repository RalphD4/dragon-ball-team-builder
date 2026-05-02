from backend.models.Team import Team
from .character_service import filter_by_tag
from backend.data.database import CHARACTERS, TEAM_TAGS

#create teams 
def build_teams(characters, team_tags):
    team_list = {}  #dictionary of all teams

    for tag in team_tags: #create a team for each current team guide
        filtered = filter_by_tag(characters, tag) #keep valid characters only
        team_list[tag] = Team(tag, filtered) #key is the Tag enum, returns a team
    
    return team_list
    

#get a specific team
def get_team_by_tag(tag):
    team = TEAMS.get(tag)
    if not team:
        return None
    return team




TEAMS = build_teams(CHARACTERS, TEAM_TAGS)