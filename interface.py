import streamlit as st
import os 
import sys
sys.path.insert(0, os.path.join(os.getcwd(),'src'))

from apiUtils import getGames
from watchOrNot import watchOrNot
from watchOrNot import playedOrNot
from watchOrNot import top3
games = getGames()

st.sidebar.title("Choose Team")
st.title("Should you watch yesterday Match ?")

def watchIt(game):
    st.write("Watch It !")
    st.write(" ->link<- ")


team = st.text_input(label = "enter your team tricode",max_chars=3)


def alternatives(games,game):
    st.write("Don't waste your time, your team lost")
    st.write("You could watch :")
    alternatives = top3(games)   
    
if team is not None:
    game = playedOrNot(games,team)
    if not(game):
        st.write("Your team didn't play yesterday :(")
    else:
        if watchOrNot(game,team):
            watchIt(game)
        else:
            st.write("Don't waste your time, your team lost")
            st.write("You could watch :")
            alternatives = top3(games)

