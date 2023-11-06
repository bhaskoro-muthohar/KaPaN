import streamlit as st
import pandas as pd
import plotly.express as px

# Load temperature data
temperature_data_path = 'data/temperature_model - temperature_model.csv'
temperature_data = pd.read_csv(temperature_data_path)

# Convert date to datetime
temperature_data['date'] = pd.to_datetime(temperature_data['date'])

# Create dropdown for subdistricts
subdistricts = temperature_data['bps_kecamatan_nama'].unique()
selected_subdistrict = st.selectbox('Select Subdistrict', options=subdistricts)

# Filter data based on the selected subdistrict
filtered_data = temperature_data[temperature_data['bps_kecamatan_nama'] == selected_subdistrict]

# Plotting
fig = px.line(filtered_data, x='date', y='temperature', title=f'Temperature Over Time for {selected_subdistrict}')
# Highlight nodes where temperature is extreme
extreme_temps = filtered_data[filtered_data['is_temperature_extreme']]
fig.add_scatter(x=extreme_temps['date'], y=extreme_temps['temperature'], mode='markers', name='Extreme Temperature', marker=dict(color='red', size=8))

st.plotly_chart(fig, use_container_width=True)

# Optional: Display raw data
if st.checkbox('Show raw data'):
    st.write(filtered_data)

# Load temperature data
temperature_data_path = 'data/temperature_model - temperature_model.csv'
temperature_data = pd.read_csv(temperature_data_path)

# Convert date to datetime
temperature_data['date'] = pd.to_datetime(temperature_data['date'])

# Determine the minimum and maximum dates for the slider
min_date = temperature_data['date'].min().date()
max_date = temperature_data['date'].max().date()

st.markdown('**Temperature Map - Java Island**')
selected_date = st.slider('Select date', min_value=min_date, max_value=max_date, value=min_date, format='YYYY-MM-DD')

# Filter data for the selected date
selected_data = temperature_data[temperature_data['date'].dt.date == selected_date]

if not selected_data.empty:
    fig_map = px.scatter_geo(
        selected_data,
        lat='latitude',
        lon='longitude',
        color='temperature',
        hover_name='bps_kecamatan_nama',
        projection='natural earth',
        title=f"Temperature Data on {selected_date}"
    )

    # Update map geos
    fig_map.update_geos(
        visible=True,
        lonaxis_range=[105, 114],  # Longitude range for Java
        lataxis_range=[-8.5, -6],  # Latitude range for Java
        center={"lat": -7.25, "lon": 109.5},  # Center of the map
        projection_scale=0.9
    )

    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.write("No temperature data available for the selected date.")