import requests
import osmtogeojson
import geopandas as gpd
import pandas as pd
import json

def fetch_water_infrastructure_data():

    # gdf = gpd.read_file("/app/pipeline/src/water.geojson")
    with open("/app/pipeline/src/water.geojson") as f:
        data = json.load(f)

    gdf = gpd.GeoDataFrame.from_features(data["features"])
    gdf.to_csv("/app/pipeline/output/amsterdam_water.csv", index=False)







# def fetch_water_infrastructure_data():
#     """
#     Fetch water infrastructure data from OpenStreetMap via Overpass API.
#     """
#     print("Fetching water infrastructure data...")
#     # Overpass endpoint and query
#     overpass_url = "https://overpass-api.de/api/interpreter"
#     query = """
#     [out:json][timeout:120];
#     area(3600271110)->.searchArea;
#     (
#     node["man_made"="water_works"](area.searchArea);
#     way ["man_made"="water_works"](area.searchArea);
#     relation["man_made"="water_works"](area.searchArea);

#     node["man_made"="desalination_plant"](area.searchArea);
#     way ["man_made"="desalination_plant"](area.searchArea);
#     relation["man_made"="desalination_plant"](area.searchArea);

#     node["man_made"="wastewater_plant"](area.searchArea);
#     way ["man_made"="wastewater_plant"](area.searchArea);
#     relation["man_made"="wastewater_plant"](area.searchArea);

#     node["man_made"="pumping_station"](area.searchArea);
#     way ["man_made"="pumping_station"](area.searchArea);
#     relation["man_made"="pumping_station"](area.searchArea);

#     node["man_made"="water_tower"](area.searchArea);
#     way ["man_made"="water_tower"](area.searchArea);
#     relation["man_made"="water_tower"](area.searchArea);

#     node["man_made"="water_well"](area.searchArea);
#     way ["man_made"="water_well"](area.searchArea);
#     relation["man_made"="water_well"](area.searchArea);

#     node["man_made"="reservoir_covered"](area.searchArea);
#     way ["man_made"="reservoir_covered"](area.searchArea);
#     relation["man_made"="reservoir_covered"](area.searchArea);

#     node["water"="reservoir"](area.searchArea);
#     way ["water"="reservoir"](area.searchArea);
#     relation["water"="reservoir"](area.searchArea);
#     );
#     out body;
#     >;
#     out skel qt;
#     """

#     # Fetch data
#     response = requests.post(overpass_url, data={'data': query})
#     try:
#         osm_json = response.json()
#     except ValueError:
#         print("RESPONSE CONTENT:", response.text)
#         return

#     # Convert Overpass JSON -> GeoJSON
#     geojson = osmtogeojson.json2geojson(osm_json)

#     # Load into GeoDataFrame
#     gdf = gpd.GeoDataFrame.from_features(geojson["features"])

#     # Save CSV (geometry will be WKT text)
#     gdf.to_csv("/app/pipeline/output/amsterdam_water.csv", index=False)

#     print("Saved GeoJSON and CSV successfully.")