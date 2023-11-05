# deprecated
import duckdb
import os

def load_geojson_to_duckdb(geojson_path, table_name, db_path='db/duckdb_file.duckdb'):
    conn = duckdb.connect(db_path)
    conn.execute("PRAGMA enable_profiling")
    conn.execute("PRAGMA profiling_output='profile.log'")
    
    temp_dir = '/tmp'
    os.makedirs(temp_dir, exist_ok=True)
    conn.execute(f"PRAGMA temp_directory='{temp_dir}'")
    
    conn.execute("LOAD 'spatial'")

    try:
        query = f"CREATE TABLE {table_name} AS SELECT * FROM ST_Read('{geojson_path}')"
        conn.execute(query)
        print(f"Data from {geojson_path} has been loaded into the table {table_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Specify the path to the GeoJSON file and the desired table name
geojson_file_path = 'data/indonesia_villages_jawa_barat_converted.geojson'
geojson_table_name = 'indonesia_villages_border_geojson'

# Call the function to load the GeoJSON into DuckDB
load_geojson_to_duckdb(geojson_file_path, geojson_table_name)
