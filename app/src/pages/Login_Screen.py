import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import os


st.set_page_config(page_title="World News")

# set the header of the page
st.header('World News Homepage')

username = st.text_input("Enter your username")
password = st.text_input("Enter your password", type="password")

st.button("Login In")
st.button("New? Sign Up!")
st.button("Forgot password?")

st.image("app/src/assets/World_homepage.png", caption="Your Journey Awaits...", width=300)
#st.image([image1, image2], caption=["Image 1", "Image 2"], width=300)




