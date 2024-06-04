
from modules.nav import FullNav
import streamlit as st
from streamlit_extras.app_logo import add_logo




st.set_page_config (page_title="About", page_icon="👋")
add_logo("assets/logo.png", height=400)
st.write("# About this App")

FullNav()

st.markdown (
    """
    Testing the automatically updating feature from the server update poll thing.
    """
        )
