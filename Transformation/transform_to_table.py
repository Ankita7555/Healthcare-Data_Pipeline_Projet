import json
import csv
import os

input_file = "data/patients_masked.json"
output_file = "data/patients_table.csv"

def transform_data():

    with open(input_file, "r") as f:
        data = json.load(f)

    rows = []

    for entry in data.get("entry", []):
        patient = entry.get("resource", {})

        patient_id = patient.get("id", "")
        gender = patient.get("gender", "")
        birth_date = patient.get("birthDate", "")

        rows.append([patient_id, gender, birth_date])

    os.makedirs("data", exist_ok=True)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["patient_id", "gender", "birthDate"])
        writer.writerows(rows)

    print("FHIR data transformed into structured table.")

if __name__ == "__main__":
    transform_data()