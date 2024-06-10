import logging
import streamlit as st
from modules.nav import SideBarLinks

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(layout="wide")

st.session_state["authenticated"] = False  # faking real passworded access
SideBarLinks(show_home=True)

st.title("Diplomatic Data")

st.write("\n\n")
st.write("### Hello, which user would you like to login as?")

col1, col2, col3 = st.columns(3)

# This routes to the page for our foreign policy persona (named Anton)
# All pages that are in the format 0x are for the foreign policy persona
with col1:
    st.image("assets/anton.jpg", width=256)
    if st.button(
        "Anton Müller, a Foreign Policy Advisor at the EU",
        type="primary",
        use_container_width=True,
    ):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "Foreign Policy Advisor"
        st.session_state["first_name"] = "Anton"
        st.session_state["user_id"] = 51
        st.switch_page("pages/00_Foreign_Policy_Advisor.py")

# This routes to the page for our PR specialist persona (named Katerina)
# All pages that are in the format 1x are for the PR specialist persona
with col2:
    st.image("assets/katerina.jpg", width=256)
    if st.button(
        "Katerina Stepanov, a PR Specialist at Gazprom Oil",
        type="primary",
        use_container_width=True,
    ):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "PR Specialist"
        st.session_state["first_name"] = "Katerina"
        st.session_state["user_id"] = 52
        st.switch_page("pages/10_PR_Specialist_Home.py")

# This routes to the page for our traveler persona (named Monika)
# All pages that are in the format 2x are for the traveler persona
with col3:
    st.image("assets/monika.jpg", width=256)
    if st.button(
        "Monika José, an unemployed traveler", type="primary", use_container_width=True
    ):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "Traveler"
        st.session_state["first_name"] = "Monika"
        st.session_state["user_id"] = 53
        st.switch_page("pages/20_Traveler_Home.py")


st.write('')
st.write('')

# Switch to our sysadmin side where we can test and run the ML model
# All pages that are in the format 3x are for our sysadmin
if st.button("Login as system administrator", type="primary", use_container_width=True):
    st.session_state["authenticated"] = True
    st.session_state["role"] = "sysadmin"
    st.session_state["first_name"] = "Sysadmin"
    st.session_state["user_id"] = 41
    st.switch_page("pages/30_SysAdmin_Home.py")
