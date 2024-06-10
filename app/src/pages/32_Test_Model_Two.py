import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Train Random Forest Classifier Model")

if st.button(
    "Train the Model",
    use_container_width=True,
):
    training = requests.get("http://api:4000/models/train_prediction2")
    st.write(training.json())
    st.write(
        f"This is how we trained the random forest classifier. Here's how we trained the X values:\n{training.json()['x_train']} and here are the y values they were trained against:\n{training.json()['y_train']}."
    )
