import logging
logger = logging.getLogger()

import requests

import json

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title('ML Model Administration Page')

st.write('\n\n')
st.write('## Model 1 Maintenance')

if st.button('Train Multiple Linear Regression Model',
             type = 'primary',
             use_container_width=True):
    st.switch_page('pages/32_Test_Model_One.py')

st.write('\n\n')
st.write('## Model 2 Maintenance')

if st.button('Train Random Forest CLassifier Model',
             type = 'primary',
             use_container_width=True,
             key = 128):
    training = requests.get(f'http://api:4000/models/train_prediction2')
    st.write(training.json())
    st.write(f"This is how we trained the random forest classifier. Here's how we trained the X values:\n{training.json()['x_train']} and here are the y values they were trained against:\n{training.json()['y_train']}.")