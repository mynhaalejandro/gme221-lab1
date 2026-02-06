# GmE 221 – Laboratory Exercise 1
## Overview
This laboratory sets up a spatial analysis environment using Python and PostGIS
and performs a parcel–landuse overlay analysis.
## Environment Setup
- Python 3.x
- PostgreSQL with PostGIS
- GeoPandas, SQLAlchemy, psycopg2
## How to Run
1. Activate the virtual environment
2. Run `main.py` to test the database connection
3. Run `overlay.py` to compute landuse percentages
## Outputs
- PostGIS table: `parcel_landuse_percentage`
- Visualization in QGIS

## Reflection: Database Connection Milestone
The database connection was implemented in a Python script and by utilizing SQL command and python syntax, the spatial data were printed similarly when viewing data thru pgAdmin. This successful connection establishes Python as a computational bridge between PostGIS and analytical workflows. Python can now issue spatial queries to the database, receive geometry-aware results as GeoDataFrames and execute GIS algorithms. The system translates spatial intent into computational execution that enables seamless integration between database-stored geometries and Python-based spatial analysis tools.