import streamlit as st

st.set_page_config(
    page_title="4SKA1 Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "mailto:bhaskoro.jr@gmail.com",
        'About': "# [Click for the secret](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
    }
)

# def main():
#     st.sidebar.title("Navigation")
#     pages = {
#         "Home": home.app,
#         "Submit Form": submit_form.app,
#     }
    
#     selection = st.sidebar.radio("Go to", list(pages.keys()))
    
#     pages[selection]()

# if __name__ == "__main__":
#     from pages import home, submit_form
#     main()

st.title('Welcome to KaPaN')
st.write('by Team 4SKA1 for UN Data Hackathon 2023')

st.markdown('''
We presented a website developed to empower farmers with knowledge.

There are 3 features farmers can use:
1. Farmers can see when extreme weather will happen next
1. Farmers can see where extreme weather will happen next
1. Farmers can post updates about conditions of their fields

Members:
- Bhaskoro Muthohar
- Bagoes Rahmat Widiarso
- Figarri Keisha
- Muhammad Nassirudin
''')
