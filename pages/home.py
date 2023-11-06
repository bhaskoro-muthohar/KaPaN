import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    district_data_path = 'data/district_feature_with_extreme_mark.csv'
    district_data = pd.read_csv(district_data_path)

    district_data['date'] = pd.to_datetime(district_data['date'], format='%Y%m%d')

    cities = district_data['bps_kota_nama'].unique()
    default_city_index = list(cities).index('KABUPATEN INDRAMAYU') if 'KABUPATEN INDRAMAYU' in cities else 0
    selected_city = st.selectbox('Select City', options=cities, index=default_city_index)
    city_filtered_data = district_data[district_data['bps_kota_nama'] == selected_city]
    subdistricts = city_filtered_data['bps_kecamatan_nama'].unique()
    selected_subdistrict = st.selectbox('Select Subdistrict', options=subdistricts)
    filtered_data = city_filtered_data[city_filtered_data['bps_kecamatan_nama'] == selected_subdistrict]
    climatic_criteria = ['humidity', 'precipitation', 'windspeed', 'temperature', 'shortwavenet']
    extreme_colors = {'above': 'red', 'below': '#FFD700', 'normal': 'blue'}

    st.markdown('## Climatic Data Line Charts')

    line_chart_cols = st.columns(2)

    for i, criterion in enumerate(climatic_criteria):
        with line_chart_cols[i % 2]:
            fig = px.line(filtered_data, x='date', y=criterion, title=f'{criterion.capitalize()} Over Time for {selected_subdistrict}')

            for mark_type in ['above', 'below']:
                extreme_points = filtered_data[filtered_data[f'{criterion}_extreme_mark'] == mark_type]
                fig.add_scatter(x=extreme_points['date'], y=extreme_points[criterion], mode='markers', name=f'{mark_type.capitalize()} {criterion.capitalize()}', marker=dict(color=extreme_colors[mark_type], size=8))
            st.plotly_chart(fig, use_container_width=True)

    st.markdown('## Climatic Data Maps - Java Island')

    min_date = city_filtered_data['date'].min().date()
    max_date = city_filtered_data['date'].max().date()

    selected_date = st.slider('Select date', min_value=min_date, max_value=max_date, value=min_date, format='YYYY-MM-DD')

    selected_data = city_filtered_data[city_filtered_data['date'].dt.date == selected_date]

    st.markdown('### Climatic Maps')
    cols = st.columns(2)
    for i, criterion in enumerate(climatic_criteria):
        with cols[i % 2]:
            if not selected_data.empty:
                selected_data['color'] = selected_data[f'{criterion}_extreme_mark'].map(extreme_colors).fillna('blue')
                
                fig_map = px.scatter_geo(
                    selected_data,
                    lat='latitude',
                    lon='longitude',
                    color='color',
                    hover_name='bps_kecamatan_nama',
                    projection='natural earth',
                    title=f"{criterion.capitalize()} Data on {selected_date}"
                )

                fig_map.update_geos(
                    visible=True,
                    lonaxis_range=[105, 114],
                    lataxis_range=[-8.5, -6],
                    center={"lat": -7.25, "lon": 109.5},
                    projection_scale=0.9
                )

                fig_map.update_traces(marker=dict(color=selected_data['color'], size=10), selector=dict(mode='markers'))
                
                fig_map.update_layout(showlegend=False)
                
                st.plotly_chart(fig_map, use_container_width=True)
            else:
                st.write(f"No {criterion} data available for the selected date.")

if __name__ == "__main__":
    app()