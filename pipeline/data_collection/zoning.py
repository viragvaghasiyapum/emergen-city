import requests
import geopandas as gpd
import os

def fetch_non_residential_functional_zoning():
    """
    Fetch non-residential functional zoning data from the Amsterdam open geodata source.
    """
    print("Fetching non-residential functional zoning data...")

    NON_RES_FUNC_SRC_URL = "https://maps.amsterdam.nl/open_geodata/geojson_latlng.php?KAARTLAAG=FUNCTIEKAART&THEMA=functiekaart"
    response = requests.get(NON_RES_FUNC_SRC_URL)

    if response.status_code == 200:
        json_data = response.json()
        gdf = gpd.GeoDataFrame.from_features(json_data["features"])
        # os.makedirs("../output", exist_ok=True) 
        gdf.to_csv("/app/pipeline/output/non_residential_functional_zoning.csv", index=False)
    else:
        print("Error:", response.status_code)