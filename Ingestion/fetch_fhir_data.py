import requests
import json
import os

# FHIR Patient API endpoint
FHIR_URL = "https://hapi.fhir.org/baseR4/Patient?_count=1000"

# Folder to save data
output_folder = "data"
os.makedirs(output_folder, exist_ok=True)

def fetch_patient_data():
    try:
        response = requests.get(FHIR_URL)
        response.raise_for_status()
        data = response.json()

        file_path = os.path.join(output_folder, "patients_raw.json")

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print("FHIR patient data saved successfully.")

    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_patient_data()