import requests
import geopandas as gpd
import os

def fetch_traffic_infrastructure_data():
    """
    Fetch traffic infrastructure data from the Amsterdam open geodata source.
    """
    print("Fetching traffic infrastructure data...")

    TRAFFIC_INFRA_SRC_URL = "https://maps.amsterdam.nl/open_geodata/geojson_latlng.php?KAARTLAAG=VERKEERSLICHTEN&THEMA=verkeerslichten"
    response = requests.get(TRAFFIC_INFRA_SRC_URL)

    if response.status_code == 200:
        json_data = response.json()
        gdf = gpd.GeoDataFrame.from_features(json_data["features"])
        gdf.to_csv("/app/pipeline/output/traffic_infrastructure.csv", index=False)
    else:
        print("Error:", response.status_code)