import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import FullNav


add_logo("assets/logo.png", height=400)

st.title('Welcome to the Brussels 2024 Dialogue Sample App')

st.write("""
        This is a sample application to 
        demonstrate what you will be able to do by the 
        end of the project.  

        This may seem trivial as it is running in a
        browser, but what you aren't seeing is that 
        the code for this small app is bundled up in a 
        Docker container and deployed to the public internet
        using Fly.io.
         
        To be added: 
        - Realtime Inferencing 
        """)  

FullNav()

# st.header('World Bank Data')

# with st.echo(code_location='above'):
#     countries:pd.DataFrame = wb.get_countries()
   
#     st.dataframe(countries)

# with st.echo(code_location='above'):
#     arr = np.random.normal(1, 1, size=100)
#     test_plot, ax = plt.subplots()
#     ax.hist(arr, bins=20)

#     st.pyplot(test_plot)


# with st.echo(code_location='above'):
#     slim_countries = countries[countries['incomeLevel'] != 'Aggregates']
#     data_crosstab = pd.crosstab(slim_countries['region'], 
#                                 slim_countries['incomeLevel'],  
#                                 margins = False) 
#     st.table(data_crosstab)
