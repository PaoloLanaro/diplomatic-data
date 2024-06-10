import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks
from datetime import datetime, timedelta, date

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Profile Information")
st.divider()

st.write(f'### First Name: {st.session_state["first_name"]}')
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

try:
    start, end = st.date_input(
        "Preferred Timeline", (date1, date2), datetime.today(), format="MM.DD.YYYY"
    )
    start_date = start.strftime("%Y-%m-%d")
    end_date = end.strftime("%Y-%m-%d")
except ValueError:
    st.error("Please select valid dates.")
    st.stop()

# --------------- get countries w/o csv --------------------
# you will have to change anywhere on this page that has something like df["Country"].
# Don't forget to remove the import and line that does this
# Make a request to get a list of the countries. Will be returned as JSON
country_list = requests.get("http://api:4000/utils/countries/sorted_list")

# Create an actual list with all the countries
country_names = []
for row in country_list.json():
    country_names.append(row["country_name"])

# Log the list to confirm all countries are there
# logger.info(f'country_names: {country_names}')
# ----------------------------------------------------------

user_id = st.session_state["user_id"]
country_traveling_to = st.selectbox("Country Traveling To", country_names)
country_traveling_from = st.selectbox("Country Traveling From", country_names)

if st.button(
    "Save results", use_container_width=True, type="primary", key="save_article"
):
    # the start_date and end_date might have "possible unbound" LSP errors, but the user can see this
    # button unless they have selected both of those dates from the date selector
    data = {
        "user_id": user_id,
        "start_date": start_date,
        "end_date": end_date,
        "country_traveling_to": country_traveling_to,
        "country_traveling_from": country_traveling_from,
    }
    response = requests.post("http://api:4000/preference/preference_routes", json=data)
    if response.status_code == 200:
        st.success("Responses saved!!!")
    else:
        st.error("Uh oh, something went wrong.")
