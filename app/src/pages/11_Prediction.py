import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")
SideBarLinks()

st.title("Country Sentiment Prediction")

st.divider()

st.write("""
        For an article of your choice, enter the country it was written in and the country it was written about, 
        along with the body of the article to have the sentiment score of the text determined. For writers interested in 
        understanding the general global perception of an audience who may be reading their work, this feature is useful in
        augmenting and tailoring arguments to be more persuasive than an inital guess may indicate. 
        """)

st.write('')
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

input_container = st.container(border=True)

# making 2 columns for the general layout
col1, col2 = input_container.columns(2)

# 1st column: country dropdown and text input
with col1:
    country_from = st.selectbox(
        "Country Article's Origin",
        country_names,
        index=None,
        placeholder="Where was the article written?",
    )
    country_about = st.selectbox(
        "Country Written About",
        country_names,
        index=None,
        placeholder="What country is the article about?",
    )

# 2nd column: month slider and hour slider
with col2:
    text = st.text_area(
        "Article Text",
        "Please add your text here",
        placeholder="Add the body of your article here.",
    )

if st.button("Calculate Sentiment", type="primary", use_container_width=True):
    sentiment = requests.get(
        f"http://api:4000/models/prediction1/{text}/{country_from}/{country_about}"
    ).json()
    sentiment_guess = round(sentiment['sentiment_guess'], 5)
    sentiment_actual = sentiment['sentiment_actual']
    st.write(
        f"""The information of the article you provided has a predicted sentiment score of {sentiment_guess} 
        which can be compared to a calculation of the sentiment by the TextBlob library that has a score of {sentiment_actual}.
        """)

