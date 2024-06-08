import logging

logger = logging.getLogger()
import pandas as pd

import requests

import streamlit as st
from modules.nav import SideBarLinks
from datetime import datetime, timedelta, date
st.set_page_config(layout="wide")

SideBarLinks()

st.title("Profile Information")
st.divider()

st.write(f'### First Name: {st.session_state["first_name"]}')
st.write(f'### Last Name: {st.session_state["last_name"]}')
st.write(f'### Job Description: {st.session_state["role"]}')

st.divider()

st.write("## User Preferences")

st.divider()

# range based select. maximum date of december 31st of the next full year. defaults to the next week 
date1 = datetime.now() + timedelta(days=7)
date2 = datetime.now() + timedelta(days=14)
next_year = date1.year + 1
range_cutoff = date(next_year, 12, 31)
next_week = datetime.now() + timedelta(days=7)

st.date_input("Preferred Timeline", (date1, date2), datetime.today(), format="MM.DD.YYYY")

# --------------- get countries w/o csv --------------------
# you will have to change anywhere on this page that has something like df["Country"].
# Don't forget to remove the import and line that does this
# Make a request to get a list of the countries. Will be returned as JSON
country_list = requests.get('http://api:4000/utils/countries/sorted_list')

# Create an actual list with all the countries
country_names = []
for row in country_list.json():
    country_names.append(row['country_name'])

# Log the list to confirm all countries are there
# logger.info(f'country_names: {country_names}')
# ----------------------------------------------------------

st.selectbox("News Subject Country", country_names)
st.selectbox("News Source Country", country_names)

st.write("")

col1, col2 = st.columns(2)


