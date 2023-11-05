import duckdb
import os

def create_table(conn, table_name, schema):
    create_stmt = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
    conn.execute(create_stmt)

def init_db(db_path='db/duckdb_file.duckdb'):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = duckdb.connect(db_path)

    conn.execute("INSTALL 'spatial'")
    conn.execute("LOAD 'spatial'")

    table_schemas = {
        "precipitation": """
            latitude DOUBLE,
            longitude DOUBLE,
            value DOUBLE,
            date DATE
        """,
        "indonesia_villages_border_geojson": """
            province VARCHAR,
            district VARCHAR,
            sub_district VARCHAR,
            village VARCHAR,
            border POLYGON_2D
        """
    }

    for table_name, schema in table_schemas.items():
        create_table(conn, table_name, schema)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
