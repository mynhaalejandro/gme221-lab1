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

## Reflection: Overlay Analysis Milestone
The overlay analysis script demonstrates the computational execution of spatial algorithms by performing parcel-landuse intersection operations. Using ST_Intersects and ST_Intersection functions in PostGIS, the system identifies geometric overlaps and calculates landuse area percentages for each parcel. This workflow combines database-side spatial processing with Python-based data manipulation that transforms raw geometries into quantified spatial relationships. The resulting parcel_landuse_percentage table represents the transition from spatial data access to analytical output that enables evidence-based land use assessment and decision-making.

## Reflection: Visualization and Interpretation Milestone
The QGIS visualization reveals the outcomes of computational spatial analysis that displays parcel-landuse relationships as geometric features with calculated percentage attributes. The percentages align with parcel shapes which shows an expected distributions where larger landuse polygons dominate smaller parcels. The CRS choice affects measurement accuracy as area calculations depend on projected coordinate systems rather than geographic coordinates. Geometry quality impacts results through vertex precision and topology consistency. The scale influences interpretation by determining the level of spatial detail captured in the overlay operation. This visualization demonstrates that maps display algorithmic results requires understanding of the underlying computational steps to properly interpret spatial patterns and validate analytical outcomes.
