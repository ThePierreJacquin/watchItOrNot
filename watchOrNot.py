import os 
import sys
sys.path.insert(0, os.path.join(os.getcwd(),'src'))
from apiUtils import getLastGame


def watchOrNot(boxscore:dict,team:str,seuil):
    teams = list(boxscore.keys())
    if team == teams[0]:
        scoreF = boxscore[teams[0]]
        scoreA = boxscore[teams[1]] 
    else:
        scoreA = boxscore[teams[0]]
        scoreF = boxscore[teams[1]] 
    if scoreA-seuil < scoreF: 
        return True
    return False

