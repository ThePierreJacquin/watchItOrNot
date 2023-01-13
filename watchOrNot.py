import os 
import sys
sys.path.insert(0, os.path.join(os.getcwd(),'src'))
from apiUtils import getLastGame


def watchOrNot(team:str):
    game = getLastGame(team)
    scoreF = game[team]
    scoreA = game[(game.keys()-{team}).pop()] 
    if scoreA-10 < scoreF: ####faire le traitement dès le début
        return True
    return False

