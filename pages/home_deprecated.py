# import streamlit as st
# import duckdb
# import pandas as pd
# import plotly.express as px
# import plotly.figure_factory as ff


# # dummy data for the crop calendar
# crop_data = [
#     dict(Task="Crop A", Start='2023-01-01', Finish='2023-02-28', Resource='Planting'),
#     dict(Task="Crop B", Start='2023-03-01', Finish='2023-04-15', Resource='Growing'),
#     dict(Task="Crop C", Start='2023-04-16', Finish='2023-06-30', Resource='Harvesting'),
# ]

# def adjust_annotation_position(annotations, input, default_ay=-40):
#     same_day_events = [ann for ann in annotations if ann['x'] == input['Date'] and ann['y'] == input['Task Index']]
#     return default_ay - (len(same_day_events) * 20)

# # Dummy user inputs for specific events, including multiple events on the same date
# user_inputs = [
#     dict(Task="Crop A", Date='2023-02-15', Event='Banjir'),
#     dict(Task="Crop A", Date='2023-02-15', Event='Longsor'),
#     dict(Task="Crop B", Date='2023-03-20', Event='Pupuk Mahal Bosku'),
#     dict(Task="Crop C", Date='2023-05-15', Event='Cangkul cangkul yang dalam'),
#     dict(Task="Crop C", Date='2023-05-15', Event='Menunggu panen'),
# ]

# selected_crops = st.multiselect('Select crops to display', options=[task['Task'] for task in crop_data], default=[task['Task'] for task in crop_data])

# filtered_crop_data = [task for task in crop_data if task['Task'] in selected_crops]

# fig = ff.create_gantt(filtered_crop_data, index_col='Resource', title='Crop Calendar', show_colorbar=True, group_tasks=True)

# annotations = []
# for input in user_inputs:
#     if input['Task'] in selected_crops:
#         task_index = [i for i, task in enumerate(filtered_crop_data) if task['Task'] == input['Task']][0]
#         ay_offset = adjust_annotation_position(annotations, {'Date': input['Date'], 'Task Index': task_index})
#         hover_text = f"{input['Event']} on {input['Date']}"
#         annotations.append(dict(
#             x=input['Date'],
#             y=task_index,
#             text=input['Event'],
#             hovertext=hover_text,
#             showarrow=True,
#             arrowhead=7,
#             ax=0,
#             ay=ay_offset
#         ))

# for task in filtered_crop_data:
#     task['hovertext'] = f"{task['Task']}<br>Start: {task['Start']}<br>Finish: {task['Finish']}"

# fig['layout']['annotations'] = annotations

# fig.update_layout(hovermode='closest')

# st.plotly_chart(fig, use_container_width=True)

# conn = duckdb.connect('db/duckdb_file.duckdb')

# query_date_range = "SELECT MIN(date) as min_date, MAX(date) as max_date FROM precipitation"
# date_range = conn.execute(query_date_range).fetchdf()
# min_date = pd.to_datetime(date_range['min_date'].iloc[0]).date()
# max_date = pd.to_datetime(date_range['max_date'].iloc[0]).date()

# st.markdown('**Precipitation Map - Java Island**')
# selected_date = st.slider('Select date', min_value=min_date, max_value=max_date, value=min_date, format='YYYY-MM-DD')

# # Fetch data for the selected date
# query = f"""
# SELECT latitude, longitude, value, date
# FROM precipitation
# WHERE date = '{selected_date}'
# AND latitude BETWEEN -8.5 AND -6.0
# AND longitude BETWEEN 105.0 AND 114.0
# """
# precipitation_data = conn.execute(query).fetchdf()

# # Close the database connection
# conn.close()

# if not precipitation_data.empty:
#     fig_map = px.scatter_geo(
#         precipitation_data,
#         lat='latitude',
#         lon='longitude',
#         color='value',
#         hover_name='date',
#         projection='natural earth'
#     )

#     fig_map.update_geos(
#         visible=True,
#         lonaxis_range=[105, 114],  # Longitude range for Java
#         lataxis_range=[-8.5, -6],  # Latitude range for Java
#         center={"lat": -7.25, "lon": 109.5},  # Center of the map
#         projection_scale=0.9
#     )

#     st.plotly_chart(fig_map, use_container_width=True)
# else:
#     st.write("No data available for the selected date.")