import duckdb
import pandas as pd
from tqdm import tqdm

def load_csv_to_db(csv_path, table_name, db_path='db/duckdb_file.duckdb'):
    df = pd.read_csv(csv_path)
    
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    
    conn = duckdb.connect(db_path)
    
    conn.execute('BEGIN TRANSACTION;')

    # Insert data from DataFrame into DuckDB table with a progress bar
    columns = ', '.join(df.columns)
    placeholders = ', '.join(['?'] * len(df.columns))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Using tqdm to show progress in chunks
    for chunk in tqdm(
            [df[i:i+1000] for i in range(0, df.shape[0], 1000)],
            desc=f"Loading data into {table_name}",
            unit="chunk"
        ):
        conn.executemany(insert_query, chunk.values.tolist())

    # Commit changes and close the connection
    conn.execute('COMMIT;')
    conn.close()

if __name__ == "__main__":
    csv_file_path = 'data/precipitation_tab_all.csv'
    table_name = 'precipitation'
    
    # Load the CSV data into the database
    load_csv_to_db(csv_file_path, table_name)
