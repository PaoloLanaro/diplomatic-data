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

st.write(formatted_list_string)

if st.button('Search for articles',
             type='primary',
             use_container_width=True):
    requests.post('http://api:4000/article/articles', json=formatted_list_string)

