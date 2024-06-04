import streamlit as st

st.set_page_config(page_title="World News")

st.markdown("""
            <style>
            .centered {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .button-row {
                display: flex;
                justify-content: space-between;
                margin-top: 10px;
            }
            .image-row {
                display: flex;
                justify-content: space-between;
                margin-top: 100px;
            }
            </style>
            """, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>World News</h2>", unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

col1, col2, col3 = st.columns(3)
with col1:
    login_button = st.button("Login")
with col2:
    st.button("New? Sign Up")
with col3:
    st.button("Forgot Username/Password")

if login_button and username and password:
    st.session_state['username'] = username
    st.session_state['password'] = password
    st.success("Login successful!")
    st.write("[Go to Dashboard](?page=dashboard)")

if login_button and not username:
    st.error("Please enter your username.")

if login_button and not password:
    st.error("Please enter your password.")
