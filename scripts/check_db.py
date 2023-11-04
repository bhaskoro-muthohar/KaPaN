import duckdb
con = duckdb.connect('db/duckdb_file.duckdb')
# print(con.execute('SELECT * FROM precipitation LIMIT 10').fetchall())
con.table('precipitation').show()