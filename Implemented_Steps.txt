## Step-by-Step Pipeline

### Step 1: FHIR Data Ingestion
- Fetches Patient resources from a public HL7 FHIR R4 API
- Stores raw healthcare data as JSON

Key Skills:
FHIR API integration, REST endpoints, healthcare data ingestion

---

### Step 2: HIPAA-Compliant PHI Masking
- Hashes patient identifiers using SHA256
- Masks patient names
- Removes address fields

Purpose:
Demonstrates HIPAA-aware data processing and privacy preservation.

---

### Step 3: Healthcare Data Transformation
- Extracts structured fields from FHIR resources
- Converts nested JSON into analytics-ready tables

Output:
patients_table.csv containing patient_id, gender, and birthDate.

---

### Step 4: Cloud Warehouse Loading
- Loads structured patient data into BigQuery
- Simulates healthcare analytics warehouse ingestion.

---

## How to Run Locally

### Create Virtual Environment
python3 -m venv venv  
source venv/bin/activate

### Install Dependencies
pip install requests pandas google-cloud-bigquery

### Run Pipeline Steps
python ingestion/fetch_fhir_data.py  
python transformation/mask_phi.py  
python transformation/transform_to_table.py  
python warehouse/load_bigquery.py

---

## Security and Compliance Notes

This project uses public synthetic FHIR data only.

HIPAA-related practices demonstrated:

- PHI masking
- Data minimization
- Governance-aware transformations

No real patient data is used.

---

## Future Enhancements

- Add dbt models for healthcare analytics layer
- Implement incremental FHIR ingestion
- Add Airflow or Prefect orchestration
- Partitioned tables in BigQuery
- Observations and Encounters resource modeling


