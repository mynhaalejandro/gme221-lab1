# Description:
# This script establishes a connection to a PostGIS-enabled PostgreSQL database
# and verifies access by querying a spatial table.

import geopandas as gpd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "gme221"
user = "mynha"
password = "P@ssw0rd"
# URL-encode the password
password_encoded = quote_plus(password)

# Create the connection string
conn_str = f"postgresql+psycopg2://{user}:{password_encoded}@{host}:{port}/{dbname}"
# Create the database engine
engine = create_engine(conn_str)
# Test query: read a spatial table
query = "SELECT * FROM public.parcel"
gdf = gpd.read_postgis(query, engine, geom_col="geom")
print(gdf.head())