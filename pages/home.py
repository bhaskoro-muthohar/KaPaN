def app():
    import streamlit as st
    import pandas as pd
    import plotly.express as px


    # Load district feature data
    district_data_path = 'data/district_feature_with_extreme_mark.csv'
    district_data = pd.read_csv(district_data_path)

    # Convert date to datetime
    district_data['date'] = pd.to_datetime(district_data['date'], format='%Y%m%d')

    # Create dropdown for cities
    cities = district_data['bps_kota_nama'].unique()
    default_city_index = list(cities).index('KABUPATEN INDRAMAYU') if 'KABUPATEN INDRAMAYU' in cities else 0
    selected_city = st.selectbox('Select City', options=cities, index=default_city_index)

    # Filter data based on the selected city
    city_filtered_data = district_data[district_data['bps_kota_nama'] == selected_city]

    # Create dropdown for subdistricts based on the selected city
    subdistricts = city_filtered_data['bps_kecamatan_nama'].unique()
    selected_subdistrict = st.selectbox('Select Subdistrict', options=subdistricts)

    # Further filter data based on the selected subdistrict
    filtered_data = city_filtered_data[city_filtered_data['bps_kecamatan_nama'] == selected_subdistrict]

    # Climatic criteria columns
    climatic_criteria = ['humidity', 'precipitation', 'windspeed', 'temperature', 'shortwavenet']

    # Define colors for extreme points
    extreme_colors = {'above': 'red', 'below': '#FFD700', 'normal': 'green'}

    # Plotting multiple line charts for each climatic criterion with extreme marks
    st.markdown('## Climatic Data Line Charts')

    n_col = 2
    line_chart_cols = st.columns(n_col)

    # Use enumerate to get the index and the criterion
    for i, criterion in enumerate(climatic_criteria):
        with line_chart_cols[i % n_col]:
            fig = px.line(filtered_data, x='date', y=criterion, title=f'{criterion.capitalize()} Over Time for {selected_subdistrict}')
            fig.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ))

            # Add extreme points
            for mark_type in ['above', 'below']:
                extreme_points = filtered_data[filtered_data[f'{criterion}_extreme_mark'] == mark_type]
                fig.add_scatter(x=extreme_points['date'], y=extreme_points[criterion], mode='markers', name=f'{mark_type.capitalize()} {criterion.capitalize()}', marker=dict(color=extreme_colors[mark_type], size=8))
            st.plotly_chart(fig, use_container_width=True)

    # Add a header to group the map charts
    st.markdown('## Climatic Data Maps - Java Island')

    # Determine the minimum and maximum dates for the slider
    min_date = city_filtered_data['date'].min().date()
    max_date = city_filtered_data['date'].max().date()

    selected_date = st.slider('Select date', min_value=min_date, max_value=max_date, value=min_date, format='YYYY-MM-DD')

    # Filter data for the selected date within the selected city
    selected_data = city_filtered_data[city_filtered_data['date'].dt.date == selected_date]

    # Create columns for map charts
    st.markdown('### Climatic Maps')
    cols = st.columns(n_col)
    for i, criterion in enumerate(climatic_criteria):
        with cols[i % n_col]:
            if not selected_data.empty:
                fig_map = px.scatter_geo(
                    selected_data,
                    lat='latitude',
                    lon='longitude',
                    color=criterion,
                    hover_name='bps_kecamatan_nama',
                    projection='natural earth',
                    title=f"{criterion.capitalize()} Data on {selected_date}"
                )
                fig.update_layout(coloraxis_colorbar=dict(
                    len=0.5,
                    xanchor="right", x=0.1,
                    yanchor='bottom', y=0.1,
                    thickness=10,
                ))
                # Update map geos
                fig_map.update_geos(
                    visible=True,
                    lonaxis_range=[105, 114],
                    lataxis_range=[-8.5, -6],
                    center={"lat": -7.25, "lon": 109.5},
                    projection_scale=0.9
                )
                st.plotly_chart(fig_map, use_container_width=True)
            else:
                st.write(f"No {criterion} data available for the selected date.")

if __name__ == "__main__":
    app()