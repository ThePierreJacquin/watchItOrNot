import os 
import sys
sys.path.insert(0, os.path.join(os.getcwd(),'src'))

#Compute if the game should be wwatched
def watchOrNot(boxscore:dict,team:str,threshold):
    teams = list(boxscore.keys())
    if team == teams[0]:
        scoreF = boxscore[teams[0]]
        scoreA = boxscore[teams[1]] 
    else:
        scoreA = boxscore[teams[0]]
        scoreF = boxscore[teams[1]] 
    if scoreA-threshold < scoreF: 
        return True
    return False

