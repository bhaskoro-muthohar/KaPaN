# deprecated

import duckdb
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import ast

conn = duckdb.connect(database='db/duckdb_file.duckdb', read_only=False)

if not conn.execute("SHOW EXTENSIONS;").fetchdf()['name'].str.contains('spatial').any():
    conn.execute("INSTALL 'spatial';")
    conn.execute("LOAD 'spatial';")

with open('data/indonesia_villages_jawa_barat.geojson', 'r') as myfile:
    data = pd.json_normalize(ast.literal_eval(myfile.read()))

data['geometry'] = data['border'].apply(lambda x: Polygon(x))

village_geo_df = gpd.GeoDataFrame(data, geometry='geometry')

village_geo_df.crs = "EPSG:4326"

create_table_query = """
CREATE TABLE indonesia_villages_jawa_barat (
    province VARCHAR,
    district VARCHAR,
    sub_district VARCHAR,
    village VARCHAR,
    geom GEOMETRY
)
"""
conn.execute(create_table_query)

for index, row in village_geo_df.iterrows():
    insert_query = f"""
    INSERT INTO indonesia_villages_jawa_barat (province, district, sub_district, village, geom)
    VALUES (
        '{row['province'].replace("'", "''")}',
        '{row['district'].replace("'", "''")}',
        '{row['sub_district'].replace("'", "''")}',
        '{row['village'].replace("'", "''")}',
        '{row['geometry'].wkt}'
    )
    """
    conn.execute(insert_query)

conn.commit()
conn.close()
