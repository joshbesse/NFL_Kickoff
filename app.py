import streamlit as st

# set page configs
st.set_page_config(
    page_title="NFL Kickoff Analysis",
    page_icon="🏈",
    layout="wide"
)

# remove top white space
st.markdown("""
    <style>
        .block-container {
            padding-top: 2.5rem;
        }
    </style>
""", unsafe_allow_html=True)
