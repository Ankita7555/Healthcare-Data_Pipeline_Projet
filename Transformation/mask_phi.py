import json
import hashlib
import os

input_file = "data/patients_raw.json"
output_file = "data/patients_masked.json"

def hash_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

def mask_name(name_list):
    if not name_list:
        return "REDACTED"
    given = name_list[0].get("given", [""])[0]
    family = name_list[0].get("family", "")
    return f"{given[:1]}*** {family[:1]}***"

def mask_phi():
    with open(input_file, "r") as f:
        data = json.load(f)

    for entry in data.get("entry", []):
        patient = entry.get("resource", {})

        # Hash patient ID
        if "id" in patient:
            patient["id"] = hash_value(patient["id"])

        # Mask patient name
        if "name" in patient:
            patient["name"] = mask_name(patient["name"])

        # Remove address (simulate HIPAA safe handling)
        patient.pop("address", None)

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print("HIPAA-style masking complete. Masked file created.")

if __name__ == "__main__":
    mask_phi()