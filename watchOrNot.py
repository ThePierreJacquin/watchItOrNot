import os 
import sys
sys.path.insert(0, os.path.join(os.getcwd(),'src'))

from apiUtils import getGames
games = getGames()

def playedOrNot(games:dict,team:str):
    for game in games:
        if game["homeTeam"]["teamTricode"] == team or game["awatTeam"]["teamTricode"] == team :
                return game
    return False

def watchOrNot(game:dict,team:str):
    if game["homeTeam"]["teamTricode"] == team:
        if game["homeTeam"]["score"] - game["awayTeam"]["score"] > -5:
            return True
        else:
            return False
    return False
    
def top3(gales:dict):
    return "Hey"



