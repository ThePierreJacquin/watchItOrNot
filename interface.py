import streamlit as st
import os,sys
import streamlit as st
import base64
sys.path.insert(0, os.path.join(os.getcwd(),'src'))
from watchOrNot import watchOrNot
from apiUtils import getLastGame,getLink

if "seuil" not in st.session_state:
    st.session_state.seuil = 10
st.title("Should I watch yesterday's match ?")
above = st.container()
above.empty()
col1,col2,col3 = st.columns([1,1,1])
below = st.container()
below.empty()

st.markdown("""
<style>
p {
    font-size:20px !important;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def watchIt(game):
    below.write("Watch It !")
    below.write(getLink(game))

def main():
    if st.session_state.team != "---":
        game = getLastGame(st.session_state.team)
        teams = list(game.keys())
        with col1:
            render_svg(open("images/"+teams[0]+".svg").read())
        with col2:
            render_svg(open('images/VS.svg').read())
        with col3:
            render_svg(open("images/"+teams[1]+".svg").read())
        
        if watchOrNot(game,st.session_state.team,st.session_state.seuil):
            watchIt(game)
        else:
            below.write("Don't waste your time, your team lost")
with above:
    btMns,text,btPs = st.columns([1,10,1])
    
    if btMns.button(":heavy_minus_sign:"):
        st.session_state.seuil -=1
    if btPs.button(":heavy_plus_sign:"):
        st.session_state.seuil +=1
    text.write("'I don't want to watch if my team lost by more than " + str(st.session_state.seuil) + " points'")
    
    teamTricodes = ["---","ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET","GSW","HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHX","POR","SAC","SAS","TOR","UTA","WAS"]
    above.selectbox("Select your team abbreviation",teamTricodes,key="team",on_change=main,label_visibility="collapsed")
    
