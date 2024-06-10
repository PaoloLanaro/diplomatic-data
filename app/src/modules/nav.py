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
    st.sidebar.page_link("pages/00_Foreign_Policy_Advisor.py", label="Anton's Home", icon='👮‍♂️')

def ForeignPolicyProfileNav():
    st.sidebar.page_link("pages/01_Profile_View.py", label="Profile")

def ForeignPolicyArticleNav():
    st.sidebar.page_link("pages/02_Add_Article.py", label="Add an Article")

def ForeignPolicyArticleViewNav():
    st.sidebar.page_link("pages/03_Foreign_Policy_Article_View.py", label="View an Article")

def ForeignPolicyRandomForestNav():
    st.sidebar.page_link("pages/04_Random_Forest.py", label="Country from article prediction")

## ------------------------ pr_specialist page nav ------------------------
def PRHomeNav():
    st.sidebar.page_link("pages/10_PR_Specialist_Home.py", label="Katerina's Home", icon='👩‍💼')

def PredictionNav():
    st.sidebar.page_link("pages/11_Prediction.py", label="Country Prediction")

def ArticleViewNav():
    st.sidebar.page_link("pages/12_Article_View.py", label="View an article")

#### ------------------------ travellers page nav ---------------------------
def TravelerHomeNav():
    st.sidebar.page_link("pages/20_Traveler_Home.py", label="Monika's Home", icon='🏄‍♀️')

def UserPreferencesNav():
    st.sidebar.page_link("pages/21_User_Preferences.py", label="User Preferences") 

def ArticleSearchNav():
    st.sidebar.page_link("pages/22_Traveler_Search.py", label="Search for Articles")

#### ------------------------ sysadmin page nav ------------------------------
def SystemAdminHomeNav():
    st.sidebar.page_link("pages/30_SysAdmin_Home.py", label="Sysadmin's Home", icon='👩‍💻')

def SystemAdminTestModelOneNav():
    st.sidebar.page_link("pages/32_Test_Model_One.py", label="Test model 1")

def SystemAdminTestModelTwoNav():
    st.sidebar.page_link("pages/33_Test_Model_Two.py", label="Test model 2")
# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/diplomatic_data_white_better_better.png", width = 250)

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
        if st.session_state['role'] == 'Foreign Policy Advisor':
            ForeignPolicyAdvHomeNav()
            ForeignPolicyProfileNav()
            ForeignPolicyArticleNav()
            ForeignPolicyArticleViewNav()
            ForeignPolicyRandomForestNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'PR Specialist':
            PRHomeNav()
            PredictionNav()
            ArticleViewNav()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'Traveler':
            TravelerHomeNav()
            UserPreferencesNav()
            ArticleSearchNav()

        if st.session_state['role'] == 'sysadmin':
            SystemAdminHomeNav()
            SystemAdminTestModelOneNav()
            SystemAdminTestModelTwoNav()
    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout & Home"):
            del st.session_state['role']
            del st.session_state['authenticated']
            del st.session_state['user_id']

            if 'random_current_article' in st.session_state:
                del st.session_state['random_current_article']

            if 'random_next_article' in st.session_state:
                del st.session_state['random_next_article']

            if 'search_terms' in st.session_state:
                del st.session_state['search_terms']

            if 'num_articles' in st.session_state:
                del st.session_state['num_articles']

            if 'article_idx' in st.session_state:
                del st.session_state['article_idx'] 
            if 'articles' in st.session_state:
                del st.session_state['articles']
            st.switch_page('Home.py')
