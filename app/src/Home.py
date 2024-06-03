import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import FullNav


import streamlit as st

params = st.experimental_get_query_params()
page = params.get("page", ["login"])[0]

if page == "login":
    import Login_Screen
elif page == "dashboard":
    import Dashboard
