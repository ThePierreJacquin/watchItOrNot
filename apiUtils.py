from nba_api.stats.endpoints import TeamGameLog,boxscoresummaryv2
from nba_api.stats.static import teams

#Get last game from a team through the NBA website
def getLastGame(team:str)->dict:
    team_id = teams.find_team_by_abbreviation(team)["id"]

    game_id = TeamGameLog(team_id).get_dict()["resultSets"][0]["rowSet"][0][1]
    
    boxscore = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game_id).get_dict()["resultSets"][5]["rowSet"]
    
    boxscore_simplified = {boxscore[0][4]:boxscore[0][-1],boxscore[1][4]:boxscore[1][-1],game_id:game_id}
    
    return boxscore_simplified



#Function I used to scrap the logo from the nba website
def getLogo(team:str)->str:
    team_id = str(teams.find_team_by_abbreviation(team)["id"])
    base_url = 'https://cdn.nba.com/logos/nba/'
    url_end = '/global/L/logo.svg'
    return base_url  + team_id + url_end

#Get the official link of a game
def getLink(boxscore:dict)->tuple(str,str):
    terms = list(boxscore.keys())
    link = "[NBA Website](https://www.nba.com/game/" + terms[0].lower() + "-vs-" + terms[1].lower()  + "-" + terms[2] +"?watchFullGame)"
    mobileLink = "[NBA App](https://nba.app.link/?$deeplink_path=gametime%3A%2F%2Fgame%2F"+terms[2]+")"
    return link,mobileLink
