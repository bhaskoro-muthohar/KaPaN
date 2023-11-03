import streamlit as st
import plotly.figure_factory as ff

# Original dummy data for the crop calendar
crop_data = [
    dict(Task="Crop A", Start='2023-01-01', Finish='2023-02-28', Resource='Planting'),
    dict(Task="Crop B", Start='2023-03-01', Finish='2023-04-15', Resource='Growing'),
    dict(Task="Crop C", Start='2023-04-16', Finish='2023-06-30', Resource='Harvesting'),
]

# Create a function to adjust annotation positions to avoid overlaps
def adjust_annotation_position(annotations, input, default_ay=-40):
    same_day_events = [ann for ann in annotations if ann['x'] == input['Date'] and ann['y'] == input['Task Index']]
    return default_ay - (len(same_day_events) * 20)

# Dummy user inputs for specific events, including multiple events on the same date
user_inputs = [
    dict(Task="Crop A", Date='2023-02-15', Event='Banjir'),
    dict(Task="Crop A", Date='2023-02-15', Event='Longsor'),
    dict(Task="Crop B", Date='2023-03-20', Event='Pupuk Mahal Bosku'),
    dict(Task="Crop C", Date='2023-05-15', Event='Cangkul cangkul yang dalam'),
    dict(Task="Crop C", Date='2023-05-15', Event='Menunggu panen'),
]

# Add a filter for the user to select which crops to display
selected_crops = st.multiselect('Select crops to display', options=[task['Task'] for task in crop_data], default=[task['Task'] for task in crop_data])

# Filter the crop data based on the selected crops
filtered_crop_data = [task for task in crop_data if task['Task'] in selected_crops]

# Generate the Gantt chart with the filtered data
fig = ff.create_gantt(filtered_crop_data, index_col='Resource', title='Crop Calendar', show_colorbar=True, group_tasks=True)

# Prepare annotations with hover text
annotations = []
for input in user_inputs:
    if input['Task'] in selected_crops:
        task_index = [i for i, task in enumerate(filtered_crop_data) if task['Task'] == input['Task']][0]
        ay_offset = adjust_annotation_position(annotations, {'Date': input['Date'], 'Task Index': task_index})
        # Add hover text to the annotation
        hover_text = f"{input['Event']} on {input['Date']}"
        annotations.append(dict(
            x=input['Date'],
            y=task_index,
            text=input['Event'],
            hovertext=hover_text,
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=ay_offset
        ))

# Add hover information to the tasks
for task in filtered_crop_data:
    task['hovertext'] = f"{task['Task']}<br>Start: {task['Start']}<br>Finish: {task['Finish']}"

# Apply the annotations to the figure
fig['layout']['annotations'] = annotations

# Set hover mode to show annotations
fig.update_layout(hovermode='closest')

# Display the Gantt chart
st.plotly_chart(fig, use_container_width=True)