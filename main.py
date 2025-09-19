from pipeline.data_collection.zoning import fetch_non_residential_functional_zoning
from pipeline.data_collection.traffic import fetch_traffic_infrastructure_data
from pipeline.data_collection.water import fetch_water_infrastructure_data
from pipeline.data_collection.power import fetch_power_infrastructure_data
from pipeline.data_collection.telecom import fetch_telecom_infrastructure_data
from pipeline.data_collection.other_pipeline import fetch_other_pipeline_infrastructure_data

if __name__ == "__main__":
    print("\n\nProject: Emergen City (Amsterdam)\n\n")

    while True:
        print("\nChoose an option:")
        print("1. Run ETL - Zoning")
        print("2. Run ETL - Traffic")
        print("3. Run ETL - Water")
        print("4. Run ETL - Power")
        print("5. Run ETL - Telecom")
        print("6. Run ETL - Other Pipelines")
        print("7. Exit")

        choice = input("> ")

        if choice == "1":
            fetch_non_residential_functional_zoning()
        elif choice == "2":
            fetch_traffic_infrastructure_data()
        elif choice == "3":
            fetch_water_infrastructure_data()
        elif choice == "4":
            fetch_power_infrastructure_data()
        elif choice == "5":
            fetch_telecom_infrastructure_data()
        elif choice == "6":
            fetch_other_pipeline_infrastructure_data()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 7.")