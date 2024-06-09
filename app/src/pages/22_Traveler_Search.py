import logging

import json

logger = logging.getLogger()
import pandas as pd

import requests
import string

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

def format_string(raw_string):
    # remove any punctuation, remove whitespace, and split into a list
    punc_removed_words = ''
    for char in raw_string:
        if char not in string.punctuation:
            punc_removed_words += char
    middle = punc_removed_words.split(' ')
    return_val = list(filter(None, middle))
    return return_val

st.title('Article Search')

st.divider()

unfiltered_words = st.text_input('Please enter some keywords for a search!', placeholder='Search Terms')

formatted_list_string = format_string(unfiltered_words)

num_articles = 0
article_idx = 0
show_articles = False
articles_json = []

if st.button('Search for articles',
             type='primary',
             use_container_width=True):
    articles = requests.post('http://api:4000/article/articles', json=formatted_list_string)
    articles_json = articles.json()
    if articles.status_code == 200:
        show_articles = True

    num_articles = len(articles_json)
    
if show_articles:
    if num_articles != 0: 
        st.write('# Title')
        st.write(f'#### Published on {articles_json[article_idx]["publication_date"]}')
        st.write(f'{articles_json[article_idx]["url"]}')
        st.divider()
        st.write('### Article Content')
        st.write(articles_json[article_idx]['content'])
        st.write(f'#### From: {articles_json[article_idx]["country_name"]}')
        if st.button('Next article',
                     use_container_width = True):
            article_idx += 1
            if article_idx >= num_articles:
                article_idx = 0
    else:
        st.write('# --No articles matched your search terms--')
