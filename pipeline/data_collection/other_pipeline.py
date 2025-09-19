import json
import requests
import osmtogeojson
import geopandas as gpd
import pandas as pd


def fetch_other_pipeline_infrastructure_data():

    # gdf = gpd.read_file("/app/pipeline/src/water.geojson")
    with open("/app/pipeline/src/other_pipelines.geojson") as f:
        data = json.load(f)

    gdf = gpd.GeoDataFrame.from_features(data["features"])
    gdf.to_csv("/app/pipeline/output/amsterdam_other_pipeline.csv", index=False)

# def fetch_pipeline_infrastructure_data():
#   # Overpass endpoint and query
#   overpass_url = "https://overpass-api.de/api/interpreter"
#   query = """
#   [out:json][timeout:120];

#   // Get Amsterdam boundary
#   {{geocodeArea:Amsterdam}}->.searchArea;

#   // PIPELINES + PIPELINE FEATURES
#   (
#     // Pipelines
#     way ["man_made"="pipeline"](area.searchArea);
#     relation["man_made"="pipeline"](area.searchArea);

#     // Pipeline features
#     node["pipeline"="valve"](area.searchArea);
#     way ["pipeline"="valve"](area.searchArea);
#     relation["pipeline"="valve"](area.searchArea);

#     node["pipeline"="substation"](area.searchArea);
#     way ["pipeline"="substation"](area.searchArea);
#     relation["pipeline"="substation"](area.searchArea);

#     node["pipeline"="flare"](area.searchArea);
#     way ["pipeline"="flare"](area.searchArea);
#     relation["pipeline"="flare"](area.searchArea);
#   );

#   // Output all geometries
#   out body;
#   >;
#   out skel qt;
#   """

#   # Fetch data
#   response = requests.post(overpass_url, data={'data': query})
#   osm_json = response.json()

#   # Convert Overpass JSON -> GeoJSON
#   geojson = osmtogeojson.json2geojson(osm_json)

#   # Load into GeoDataFrame
#   gdf = gpd.GeoDataFrame.from_features(geojson["features"])

#   # Save CSV (geometry will be WKT text)
#   gdf.to_csv("/app/pipeline/output/amsterdam_water.csv", index=False)

#   print("Saved GeoJSON and CSV successfully.")