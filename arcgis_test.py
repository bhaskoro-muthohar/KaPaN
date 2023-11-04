import streamlit as st

# Define the URL of the ArcGIS map, potentially with parameters set to focus on Java Island
arcgis_map_url = "https://www.arcgis.com/home/webmap/viewer.html?center=109.5,-7.25&level=7"

# Embed the map using an iframe in a Streamlit markdown
st.markdown(
    f"""
    <iframe
        src="{arcgis_map_url}"
        width="600"
        height="450"
        style="border:none;">
    </iframe>
    """,
    unsafe_allow_html=True
)