import json
import requests
import osmtogeojson
import geopandas as gpd
import pandas as pd


def fetch_power_infrastructure_data():

    # gdf = gpd.read_file("/app/pipeline/src/water.geojson")
    with open("/app/pipeline/src/power.geojson") as f:
        data = json.load(f)

    gdf = gpd.GeoDataFrame.from_features(data["features"])
    gdf.to_csv("/app/pipeline/output/amsterdam_power.csv", index=False)


# def fetch_power_infrastructure_data():
#   # Overpass endpoint and query
#   overpass_url = "https://overpass-api.de/api/interpreter"
#   query = """
#   [out:json][timeout:180];

#   // Define Amsterdam administrative boundary
#   {{geocodeArea:Amsterdam}}->.searchArea;

#   // POWER INFRASTRUCTURE
#   (
#     // Generators
#     node["power"="generator"](area.searchArea);
#     way ["power"="generator"](area.searchArea);
#     relation["power"="generator"](area.searchArea);

#     // Power plants
#     node["power"="plant"](area.searchArea);
#     way ["power"="plant"](area.searchArea);
#     relation["power"="plant"](area.searchArea);

#     // Power lines
#     way ["power"="line"](area.searchArea);
#     relation["power"="line"](area.searchArea);
#     way ["power"="minor_line"](area.searchArea);
#     relation["power"="minor_line"](area.searchArea);
#     way ["power"="cable"](area.searchArea);
#     relation["power"="cable"](area.searchArea);
#     way ["power"="minor_cable"](area.searchArea);
#     relation["power"="minor_cable"](area.searchArea);

#     // Substations
#     node["power"="substation"](area.searchArea);
#     way ["power"="substation"](area.searchArea);
#     relation["power"="substation"](area.searchArea);

#     // Transformers
#     node["power"="transformer"](area.searchArea);
#     way ["power"="transformer"](area.searchArea);
#     relation["power"="transformer"](area.searchArea);

#     // Switches
#     node["power"="switch"](area.searchArea);
#     way ["power"="switch"](area.searchArea);
#     relation["power"="switch"](area.searchArea);

#     // Compensators
#     node["power"="compensator"](area.searchArea);
#     way ["power"="compensator"](area.searchArea);
#     relation["power"="compensator"](area.searchArea);

#     // Towers, poles, portals
#     node["power"="pole"](area.searchArea);
#     way ["power"="pole"](area.searchArea);
#     relation["power"="pole"](area.searchArea);

#     node["power"="tower"](area.searchArea);
#     way ["power"="tower"](area.searchArea);
#     relation["power"="tower"](area.searchArea);

#     node["power"="portal"](area.searchArea);
#     way ["power"="portal"](area.searchArea);
#     relation["power"="portal"](area.searchArea);
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