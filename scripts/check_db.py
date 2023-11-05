import duckdb
con = duckdb.connect('db/duckdb_file.duckdb')
# print(con.execute('SELECT * FROM precipitation LIMIT 10').fetchall())
# con.table('precipitation').show()

# con.execute("""
# ALTER TABLE reports ADD COLUMN IF NOT EXISTS province VARCHAR;
# ALTER TABLE reports ADD COLUMN IF NOT EXISTS regency VARCHAR;
# ALTER TABLE reports ADD COLUMN IF NOT EXISTS subdistrict VARCHAR;
# """)

# con.execute("DROP SEQUENCE IF EXISTS report_id_seq")
# con.execute("DROP TABLE IF EXISTS reports")
# con.execute("SELECT NEXTVAL('report_id_seq');")

# Create a sequence if it does not exist
con.execute("CREATE SEQUENCE IF NOT EXISTS report_id_seq;")

# Try to get the next value of the sequence
try:
    next_val = con.execute("SELECT NEXTVAL('report_id_seq');").fetchone()[0]
    print("Next sequence value is:", next_val)
except Exception as e:
    print("An error occurred:", e)