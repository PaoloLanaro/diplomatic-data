import streamlit as st
import logging
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Test model 2")

number1 = st.slider("Observation 1", 0, 10, 5)

if st.button(
    "Test Model on sample input?",
    use_container_width=True,
):
    response = requests.get(f"http://api:4000/models/prediction2/{number1}")
    if response.status_code == 200:
        test = response.json()
        st.write(f"Test for input {number1} is {test}")
    else:
        st.write("Ran into an error retrieving a prediction score -- try again")
