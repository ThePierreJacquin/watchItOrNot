from nba_api.live.nba.endpoints import scoreboard

def getGames():
    games = scoreboard.ScoreBoard()
    dic = games.get_dict()
    return dic["scoreboard"]["games"]

