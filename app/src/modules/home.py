import streamlit as st

# common welcome layout for all our pages
def Welcome(): 
    st.title(f"Welcome {st.session_state['role']}, {st.session_state['first_name']}.")
    st.write("")
    st.write("")
    st.write("### What would you like to do today?")
    st.write("")
