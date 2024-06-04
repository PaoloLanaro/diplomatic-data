import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard",
    layout="centered",
    initial_sidebar_state="expanded",
)

if 'username' not in st.session_state:
    st.warning("Please log in first")
    st.write("[Go to Login](?page=login)")
    st.stop()

username = st.session_state['username']

st.title(f"Welcome, {username}")

col1, col2, col3 = st.columns(3)
with col1:
    st.button("Dashboard")
with col2:
    st.button("Profile")
with col3:
    st.button("Settings")

st.subheader("Filters")
location = st.selectbox("Location", ["Location 1", "Location 2", "Location 3"])
date_range = st.date_input("Timeframe", [])

st.subheader("Sentiment Trends")

st.subheader("Figure will go here!")

st.subheader("Notifications")
st.write("Alert -> Changes in X region")
st.write("Alert -> Trends in X region")

st.button("View Article")
