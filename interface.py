import streamlit as st
import base64
from watchOrNot import watchOrNot
from apiUtils import getLastGame,getLink
import os,sys
import streamlit as st
sys.path.insert(0, os.path.join(os.getcwd(),'src'))

#Setting the threshold for a blowout game
if "threshold" not in st.session_state:
    st.session_state.threshold = 10

#Setting Up the display
st.title("Should I watch yesterday's match ?")
above = st.container()
above.empty()
col1,col2,col3 = st.columns([1,1,1])
below = st.container()
below.empty()

#Setting up CSS style
st.markdown("""
<style>
p {
    font-size:20px !important;
    font-weight: bold;
    text-align: center;
}
[data-testid="column"] {
        width: calc(33.3333% - 1rem) !important;
        flex: 1 1 calc(33.3333% - 1rem) !important;
        min-width: calc(33% - 1rem) !important;
[data-tes]
}
div.stButton { 
    text-align: center; 
}
[data-testid="stMarkdownContainer"] {
    text-align: center;
    font-weight: normal;
}
</style>
""", unsafe_allow_html=True)

#Display a svg 
def render_svg(svg:str):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

#Get the official link for the game
def watchIt(game:dict):
    below.write("Watch It !")
    link,mobileLink = getLink(game)
    below.markdown(link, unsafe_allow_html=True)
    below.markdown(mobileLink, unsafe_allow_html=True)
    
#Main function
def main():
    if st.session_state.team != "---":
        #Get last game and display teams logo
        game = getLastGame(st.session_state.team)
        teams = list(game.keys())
        with col1:
            render_svg(open("images/"+teams[0]+".svg").read())
        with col2:
            render_svg(open('images/VS.svg').read())
        with col3:
            render_svg(open("images/"+teams[1]+".svg").read())
        
        #Compute if game should be watched and act accordingly
        if watchOrNot(game,st.session_state.team,st.session_state.threshold):
            watchIt(game)
        else:
            below.write("Don't waste your time, your team lost")

#Landing page
with above:
    st.warning("Remember to toggle 'Hide Score' on your NBA League Pass !")
    teamTricodes = ["---","ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET","GSW","HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHX","POR","SAC","SAS","TOR","UTA","WAS"]
    st.selectbox("Select your team abbreviation",teamTricodes,key="team",on_change=main,label_visibility="collapsed")
    if st.session_state.team == "---":
        
        if col1.button(":heavy_minus_sign:"):
            st.session_state.threshold -=1
        if col3.button(":heavy_plus_sign:"):
            st.session_state.threshold +=1    
        st.write("'I don't want to watch if my team lost by more than " + str(st.session_state.threshold) + " points'")   
        

    
