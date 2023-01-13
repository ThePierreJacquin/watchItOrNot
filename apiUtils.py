from nba_api.stats.endpoints import TeamGameLog,boxscoresummaryv2
from nba_api.stats.static import teams

def getLastGame(team:str):
    team_id = teams.find_team_by_abbreviation(team)["id"]

    game_id = TeamGameLog(team_id).get_dict()["resultSets"][0]["rowSet"][0][1]
    
    boxscore = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game_id).get_dict()["resultSets"][5]["rowSet"]
    
    boxscore_simplified = {boxscore[0][4]:boxscore[0][-1],boxscore[1][4]:boxscore[1][-1],game_id:game_id}
    
    return boxscore_simplified



# create the url parts that do not change
def getLogo(team:str):
    team_id = str(teams.find_team_by_abbreviation(team)["id"])
    base_url = 'https://cdn.nba.com/logos/nba/'
    url_end = '/global/L/logo.svg'
    return base_url  + team_id + url_end

def getLink(boxscore:dict):
    terms = list(boxscore.keys())
    link = "https://www.nba.com/game/" + terms[0].lower() + "-vs-" + terms[1].lower()  + "-" + terms[2] +"?watchFullGame"
    return link
