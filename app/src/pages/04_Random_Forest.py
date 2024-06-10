import requests
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title(
    f"Hello {st.session_state['first_name']}, Check out our Random Forest ML model"
)
st.divider()

st.write("""This ML model is called a Random Forest Classifier. We ask that you provide the text of an article you 
         are interested in and the country your article is being written about. Using your information, our model
         will do its best to predict the article's source country (the country it is being written from).""")


country_names = ["Russia", "China", "United States"]


st.write("")

input_container = st.container(border=True)

country = input_container.selectbox(
    "Queried country ",
    country_names,
    index=None,
    placeholder="What country was the article written about?",
)

text = input_container.text_area(
    "Article Text",
    "Please add your text here",
    placeholder="Add the body of your article here.",
)

if st.button(
    "Predict what country this has been written from",
    type="primary",
    use_container_width=True,
):
    predicted_country = requests.get(
        f"http://api:4000/models/prediction2/{text}/{country}"
    )
    st.write(
        f"The predicted country this article is written from is the {predicted_country.json()}!"
    )
    st.write("Is this correct? If not, we may need to train this thing better....")
