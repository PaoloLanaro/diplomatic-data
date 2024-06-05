import streamlit as st
import logging
logger = logging.getLogger()

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/50_About.py", label="About", icon="🧠")

#### ------------------------ foreign_policy_advisor page nav ------------------------
def ForeignPolicyAdvHomeNav():
    st.sidebar.page_link("pages/00_Foreign_Policy_Advisor.py", label="Foreign Policy Advisor Home", icon='👮‍♂️')

def ForeignPolicyProfileNav():
    st.sidebar.page_link("pages/01_Profile_View.py", label="Profile")

## ------------------------ pr_specialist page nav ------------------------
def PRHomeNav():
    st.sidebar.page_link("pages/10_PR_Specialist_Home.py", label="Home", icon='🏠')

def PredictionNav():
    st.sidebar.page_link("pages/11_Prediction.py", label="Countries Predicted Sentiment Score")

def ArticleViewNav():
    st.sidebar.page_link("pages/12_Article_View.py", label="View an article")

def ApiTestNav():
    st.sidebar.page_link("pages/99_API_Test.py", label="Test the API", icon='🛜')

#### ------------------------ travellers page nav ---------------------------
def TravelerHomeNav():
    st.sidebar.page_link("pages/20_Traveler_Home.py", label="Home", icon='🏠')

def UserPreferencesNav():
    st.sidebar.page_link("pages/21_User_Preferences.py", label="User Preferences", icon='🎭')

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/world_news_logo.png", width = 150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
       
    # Show the Home page link (the landing page) if not logged in
    if show_home and not st.session_state['authenticated']:  
        HomeNav()


    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'foreign_policy_advisor':
            ForeignPolicyAdvHomeNav()
            ForeignPolicyProfileNav()
            # WorldBankVizNav()
            # MapDemoNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'pr_specialist':
            PRHomeNav()
            PredictionNav()
            ArticleViewNav()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'traveler':
            TravelerHomeNav()
            UserPreferencesNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout & Home"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')
