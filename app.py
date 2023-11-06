import streamlit as st

st.set_page_config(
    page_title="4sk1 Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "mailto:bhaskoro.jr@gmail.com",
        'About': "# [Click for the secret](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
    }
)

def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": home.app,
        "Submit Form": submit_form.app,
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    pages[selection]()

if __name__ == "__main__":
    from pages import home, submit_form
    main()
