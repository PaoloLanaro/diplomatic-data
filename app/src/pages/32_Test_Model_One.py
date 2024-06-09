import streamlit as st
import logging
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Train Multiple Linear Regression Model")

if st.button(
    "Train the Model",
    use_container_width=True,
):
    response = requests.get("http://api:4000/models/train_prediction1")
    
    requests.post('http://api:4000/models/weight_vector', json=response.json())



    if response.status_code == 200:
        train = response.json()
        st.write(f"The bias vector for the training input after cross validation: {train}.")
    else:
        st.write("Ran into an error retrieving a prediction score -- try again.")
