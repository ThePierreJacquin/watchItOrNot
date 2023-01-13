import streamlit as st
import os,sys
import cairosvg
sys.path.insert(0, os.path.join(os.getcwd(),'src'))
from watchOrNot import watchOrNot
from apiUtils import getLastGame,getLink
from time import time
st.session_state.seuil = 5
st.title("Should you watch yesterday Match ?")
above = st.container()
above.empty()
col1,col2,col3 = st.columns([1,1,1])
below = st.container()
below.empty()

def watchIt(game):
    below.write("Watch It !")
    below.write(getLink(game))

def main():
    game = getLastGame(st.session_state.team)
    teams = list(game.keys())
    col1.image(cairosvg.svg2png(url='images/'+teams[0]+'.svg', output_width=426, output_height=240))
    col2.write(cairosvg.svg2png(url='images/VS.svg', output_width=426, output_height=240))
    col3.image(cairosvg.svg2png(url='images/'+teams[1]+'.svg', output_width=426, output_height=240))
    
    if watchOrNot(game,st.session_state.team,st.session_state.seuil):
        watchIt(game)
    else:
        below.write("Don't waste your time, your team lost", unsafe_allow_html=True)

teamTricodes = ["---","ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET","GSW","HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHX","POR","SAC","SAS","TOR","UTA","WAS"]
above.selectbox("Select your team abbreviation",teamTricodes,key="team",on_change=main)
    
