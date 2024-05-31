import streamlit as st


#### --------------------------------- General ---------------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏡')

def AboutNav():
    st.sidebar.page_link("pages/10_About.py", label="About", icon='🧠')


#### --------------------------------- something ---------------------------------

def FullNav():
    HomeNav()
    AboutNav()
