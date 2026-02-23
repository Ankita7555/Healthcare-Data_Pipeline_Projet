# FHIR Healthcare Data Pipeline with HIPAA-Compliant Processing

## Overview
This project demonstrates an end-to-end healthcare data engineering pipeline built using Python, HL7 FHIR APIs, and Google BigQuery. The pipeline simulates how real healthcare organizations ingest Electronic Health Record (EHR) data, apply HIPAA-compliant transformations, and load structured datasets into a cloud data warehouse for analytics.

The goal of this project is to showcase practical experience with:

- HL7 FHIR interoperability
- Healthcare data ingestion
- HIPAA-style PHI masking
- ETL pipeline development
- Cloud data warehousing
- Healthcare data modeling

---

## Architecture

FHIR API → Python Ingestion → HIPAA Masking → Transformation → BigQuery Warehouse

Steps included in this project:

1. Ingest patient resources from a public HL7 FHIR server
2. Apply PHI masking aligned with HIPAA data handling principles
3. Transform nested FHIR JSON into structured relational tables
4. Load curated healthcare data into BigQuery
5. Orchestrate workflow using a pipeline structure

---

## Technologies Used

- Python
- HL7 FHIR REST APIs
- Google BigQuery
- Pandas
- Requests
- VS Code Development Environment

Healthcare Concepts Demonstrated:

- Healthcare interoperability (FHIR)
- Protected Health Information (PHI) handling
- Data governance and security awareness
- Healthcare data normalization

---

## Project Structure
fhir-healthcare-pipeline/
├── ingestion/
│ └── fetch_fhir_data.py
├── transformation/
│ ├── mask_phi.py
│ └── transform_to_table.py
├── warehouse/
│ └── load_bigquery.py
├── data/
│ ├── patients_raw.json
│ ├── patients_masked.json
│ └── patients_table.csv
└── README.md