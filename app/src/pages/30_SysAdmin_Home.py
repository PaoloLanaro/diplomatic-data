import requests

import streamlit as st
from modules.nav import SideBarLinks
import numpy as np

st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("ML Model Administration Page")

st.write("\n\n")
st.write("## Model 1 Maintenance")

if st.button(
    "Train Multiple Linear Regression Model", type="primary", use_container_width=True
):
    st.switch_page("pages/32_Test_Model_One.py")

st.write("\n\n")
st.write("## Model 2 Maintenance")

if st.button(
    "Train Random Forest Classifier Model",
    type="primary",
    use_container_width=True,
    key=128,
):
    training = requests.get("http://api:4000/models/train_prediction2")
    st.write(
        f"This is how we trained the random forest classifier. Here's some of the first few X training values:\n{np.array(training.json()['x_train'])[:5]} and here are some of the y values they were trained against:\n{np.array(training.json()['y_train'])[:5]}."
    )
