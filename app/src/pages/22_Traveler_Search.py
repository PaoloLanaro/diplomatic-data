import logging
import requests
import string
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

if "search_terms" not in st.session_state:
    st.session_state["search_terms"] = ""


def format_string(raw_string):
    # remove any punctuation, remove whitespace, and split into a list
    punc_removed_words = ""
    for char in raw_string:
        if char not in string.punctuation:
            punc_removed_words += char
    middle = punc_removed_words.split(" ")
    return_val = list(filter(None, middle))
    return return_val


st.title("Article Search")

st.divider()

unfiltered_words = st.text_input(
    "Please enter some keywords for a search!", placeholder="Search Terms"
)
logger.info(f"unfiltered_words {unfiltered_words}")
formatted_list_string = format_string(unfiltered_words)

st.session_state["search_terms"] = formatted_list_string


if st.button("Search for articles", type="primary", use_container_width=True):
    if len(st.session_state["search_terms"]) != 0:
        articles = requests.post(
            "http://api:4000/article/articles", json=st.session_state["search_terms"]
        )
        articles_json = articles.json()
        if articles.status_code == 200:
            st.session_state["articles"] = articles_json
            st.session_state["num_articles"] = len(articles_json)
            st.session_state["article_idx"] = 0
    else:
        st.session_state["num_articles"] = 0
        st.error("Please input some text")

if st.button("Clear search results", use_container_width=True):
    if "search_terms" in st.session_state:
        del st.session_state['search_terms']
    if "articles" in st.session_state:
        del st.session_state['articles']
    if "num_articles" in st.session_state:
        del st.session_state['num_articles']
    if "article_idx" in st.session_state:
        del st.session_state['article_idx']

if "articles" in st.session_state:
    articles_json = st.session_state["articles"]
    article_idx = st.session_state["article_idx"]

    if st.session_state["num_articles"] != 0:
        title_request = requests.get(
            f'http://api:4000/article/title/{articles_json[article_idx]["url"]}'
        )
        title = title_request.json()
        if title_request.status_code == 200:
            st.write(f"# {title['title']}")

        st.write(f'#### Published on {articles_json[article_idx]["publication_date"]}')

        st.write(f'{articles_json[article_idx]["url"]}')

        st.divider()

        st.write("### Article Content")
        st.write(articles_json[st.session_state["article_idx"]]["content"])

        st.write(f'#### From: {articles_json[article_idx]["country_name"]}')

        if st.button("Next article", use_container_width=True):
            st.session_state["article_idx"] += 1
            if article_idx == st.session_state["num_articles"] - 1:
                st.session_state["article_idx"] = 0
    else:
        st.write("# --No articles matched your search terms--")
        st.write("# --Please try again--")
