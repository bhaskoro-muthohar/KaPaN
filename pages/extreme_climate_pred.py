import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    @st.cache
    def load_data():
        df = pd.read_csv('data/data_model.csv')
        df['date'] = pd.to_datetime(df['date'])
        return df

    df = load_data()

    st.markdown('# Extreme Climate Predictions')

    selected_date = st.select_slider(
        'Select a date for prediction',
        options=df['date'].dt.date.unique(),
        format_func=lambda x: x.strftime('%Y-%m-%d')
    )

    df_filtered_date = df[df['date'].dt.date == selected_date]

    st.write(f"Data for {selected_date}")

    climatic_properties = [
        'temperature', 'windspeed', 'shortwavenet', 'humidity', 'precipitation'
    ]

    col1, col2 = st.columns(2)

    def display_table_for_property(df, property, column):
        cols_to_display = [
            'bps_kota_nama', 'bps_kecamatan_nama',
            property, f"{property}_extreme_perc", f"is_{property}_extreme"
        ]
        df_display = df[cols_to_display]
        column.markdown(f"#### {property.capitalize()}")
        column.dataframe(df_display)

    for i, property in enumerate(climatic_properties):
        if i % 2 == 0:
            display_table_for_property(df_filtered_date, property, col1)
        else:
            display_table_for_property(df_filtered_date, property, col2)

    st.write("## Top 5 Sub-districts for Climatic Properties")

    bar_col1, bar_col2 = st.columns(2)

    def display_horizontal_bar_chart_for_property(df, property, column):
        top5_sub_districts = df.nlargest(5, property)
        color = ['red' if is_extreme else 'lightgrey' for is_extreme in top5_sub_districts[f"is_{property}_extreme"]]
        fig = px.bar(top5_sub_districts, y='bps_kecamatan_nama', x=property,
                    title=f"Top 5 Sub-districts by {property.capitalize()}",
                    labels={'bps_kecamatan_nama': 'Sub-district Name'},
                    orientation='h',
                    color_discrete_sequence=color)
        fig.update_traces(texttemplate='%{x:.2f}', textposition='outside')
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        column.plotly_chart(fig, use_container_width=True)

    for i, property in enumerate(climatic_properties):
        if i % 2 == 0:
            display_horizontal_bar_chart_for_property(df_filtered_date, property, bar_col1)
        else:
            display_horizontal_bar_chart_for_property(df_filtered_date, property, bar_col2)

if __name__ == "__main__":
    app()
