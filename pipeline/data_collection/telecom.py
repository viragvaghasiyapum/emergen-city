import json
import requests
import osmtogeojson
import geopandas as gpd



def fetch_telecom_infrastructure_data():

    # gdf = gpd.read_file("/app/pipeline/src/water.geojson")
    with open("/app/pipeline/src/telecom.geojson") as f:
        data = json.load(f)

    gdf = gpd.GeoDataFrame.from_features(data["features"])
    gdf.to_csv("/app/pipeline/output/amsterdam_telecom.csv", index=False)


# def fetch_telecom_infrastructure_data():
#     # Overpass endpoint and query
#     overpass_url = "https://overpass-api.de/api/interpreter"
#     query = """
#     [out:json][timeout:120];

#     // Get Amsterdam boundary
#     {{geocodeArea:Amsterdam}}->.searchArea;

#     // TELECOM FEATURES
#     (
#     // Telecom buildings
#     node["building"="data_center"](area.searchArea);
#     way ["building"="data_center"](area.searchArea);
#     relation["building"="data_center"](area.searchArea);

#     node["building"="data_centre"](area.searchArea);
#     way ["building"="data_centre"](area.searchArea);
#     relation["building"="data_centre"](area.searchArea);

#     node["building"="telephone_exchange"](area.searchArea);
#     way ["building"="telephone_exchange"](area.searchArea);
#     relation["building"="telephone_exchange"](area.searchArea);

#     node["telecom"="data_center"](area.searchArea);
#     way ["telecom"="data_center"](area.searchArea);
#     relation["telecom"="data_center"](area.searchArea);

#     node["telecom"="data_centre"](area.searchArea);
#     way ["telecom"="data_centre"](area.searchArea);
#     relation["telecom"="data_centre"](area.searchArea);

#     node["telecom"="exchange"](area.searchArea);
#     way ["telecom"="exchange"](area.searchArea);
#     relation["telecom"="exchange"](area.searchArea);

#     node["telecom"="central_office"](area.searchArea);
#     way ["telecom"="central_office"](area.searchArea);
#     relation["telecom"="central_office"](area.searchArea);

#     node["office"="telecommunication"](area.searchArea);
#     way ["office"="telecommunication"](area.searchArea);
#     relation["office"="telecommunication"](area.searchArea);

#     node["man_made"="telephone_office"](area.searchArea);
#     way ["man_made"="telephone_office"](area.searchArea);
#     relation["man_made"="telephone_office"](area.searchArea);

#     // Telecom cables
#     way ["communication"="line"](area.searchArea);
#     relation["communication"="line"](area.searchArea);
#     way ["communication"="cable"](area.searchArea);
#     relation["communication"="cable"](area.searchArea);

#     // Masts & towers
#     node["man_made"="mast"](area.searchArea);
#     way ["man_made"="mast"](area.searchArea);
#     relation["man_made"="mast"](area.searchArea);

#     node["man_made"="tower"](area.searchArea);
#     way ["man_made"="tower"](area.searchArea);
#     relation["man_made"="tower"](area.searchArea);

#     node["man_made"="communications_tower"](area.searchArea);
#     way ["man_made"="communications_tower"](area.searchArea);
#     relation["man_made"="communications_tower"](area.searchArea);
#     );

#     // Output with full geometry
#     out body;
#     >;
#     out skel qt;
#     """

#     # Fetch data
#     response = requests.post(overpass_url, data={'data': query})
#     osm_json = response.json()

#     # Convert Overpass JSON -> GeoJSON
#     geojson = osmtogeojson.json2geojson(osm_json)

#     # Load into GeoDataFrame
#     gdf = gpd.GeoDataFrame.from_features(geojson["features"])

#     # Save CSV (geometry will be WKT text)
#     gdf.to_csv("/app/pipeline/output/amsterdam_water.csv", index=False)

#     print("Saved GeoJSON and CSV successfully.")