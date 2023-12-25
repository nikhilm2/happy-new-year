from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
from streamlit_card import card
import random


THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "happy_24.json"


def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def run_lottie_animation():
    rain(emoji="✨", font_size=20,falling_speed=5,animation_length="infinite")
    
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name",["Fella"])[0]

st.set_page_config(page_title="Happy New Year '24", page_icon="✨")

run_lottie_animation()

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

PERSON_NAME = get_person_name()
st.header(f"Happy New Year, :blue[{PERSON_NAME}]! 🎊", anchor=False)

lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation,key="happy-2024",height=300)


st.markdown(
   
    f"Dear :red[{PERSON_NAME}], Wishing You Happy New Year filled with joy and peace. 🎉",
)

card(
    title="Press Your LUCK!",
    text="A Suprise for You...",
    image="https://www.icegif.com/wp-content/uploads/2023/03/icegif-235.gif",
    url= random.choice(["https://youtu.be/EE-xtCF3T94?si=W2H7lcnrWdtkp7UX","https://www.youtube.com/watch?v=6hlTj-cK7XU&list=PLQcpjwveNrhI3463tNa04SON2YGh9fMVH","https://youtu.be/17l66cbys_M?si=g3mwBGqacShYSuew"])
    
)

#primaryColor = "#d33682"

#backgroundColor = "#98FB98"

#secondaryBackgroundColor = "#586e75"
