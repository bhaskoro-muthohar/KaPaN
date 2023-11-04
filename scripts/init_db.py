import duckdb
import os

def init_db(db_path='db/duckdb_file.duckdb'):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = duckdb.connect(db_path)
    
    # Create the table for precipitation data
    conn.execute("""
        CREATE TABLE IF NOT EXISTS precipitation (
            latitude DOUBLE,
            longitude DOUBLE,
            value DOUBLE,
            date DATE
        )
    """)
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
