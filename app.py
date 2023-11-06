import streamlit as st

st.set_page_config(
    page_title="4sk1 Dashboard",
    page_icon="🦈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    'Report a bug': "mailto:bhaskoro.jr@gmail.com",
    'About': "# [Click for the secret](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
    }
)

st.title('KaPaN')
st.write('4sk1 Project.')