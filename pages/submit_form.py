def app():
    import streamlit as st
    import duckdb
    from datetime import datetime

    # Initialize connection to DuckDB
    conn = duckdb.connect('db/duckdb_file.duckdb', read_only=False)

    # Create the sequence and table without checking for existence
    conn.execute("""
    CREATE SEQUENCE IF NOT EXISTS report_id_seq;
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY DEFAULT NEXTVAL('report_id_seq'),
        message VARCHAR(64),
        province VARCHAR,
        regency VARCHAR,
        subdistrict VARCHAR,
        report_date DATE
    );
    """)

    # Function to insert a new report into the database
    def insert_report(message, province, regency, subdistrict, report_date):
        # Get the next sequence value to be used as the id
        next_id = conn.execute("SELECT NEXTVAL('report_id_seq');").fetchone()[0]
        # Insert the new report into the database with the new id
        conn.execute("""
            INSERT INTO reports (id, message, province, regency, subdistrict, report_date) 
            VALUES (?, ?, ?, ?, ?, ?);
            """, (next_id, message, province, regency, subdistrict, report_date))
        conn.commit()

    # Function to get all reports
    def get_reports():
        return conn.execute("SELECT * FROM reports ORDER BY report_date DESC, id DESC").fetchdf()

    # Streamlit form for report submission
    with st.form("report_form"):
        message = st.text_area("Short Message (max 64 chars)", max_chars=64)
        province = st.text_input("Province")
        regency = st.text_input("Regency")
        subdistrict = st.text_input("Subdistrict")
        report_date = st.date_input("Date of the Message", datetime.now())
        submitted = st.form_submit_button("Submit Report")

        if submitted:
            insert_report(message, province, regency, subdistrict, report_date)
            st.success("Report submitted successfully!")

    # Display reports
    st.write("Submitted Reports:")
    reports_df = get_reports()

    # Use columns to create a card-like layout for each report
    for index, report in reports_df.iterrows():
        with st.container():
            st.subheader(f"Report from {report['province']}, {report['regency']}, {report['subdistrict']}")
            st.write(f"Date: {report['report_date'].strftime('%Y-%m-%d')}")
            st.info(report['message'])

if __name__ == "__main__":
    app()