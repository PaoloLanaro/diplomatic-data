import streamlit as st
import requests
from modules.nav import SideBarLinks
import numpy as np

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Train Random Forest Classifier Model")

if st.button(
    "Train the Model",
    use_container_width=True,
):
    training = requests.get("http://api:4000/models/train_prediction2")
    st.write(
        f"This is how we trained the random forest classifier. Here's some of the first few X training values:\n{np.array(training.json()['x_train'])[:5]} and here are some of the y values they were trained against:\n{np.array(training.json()['y_train'])[:5]}."
    )
