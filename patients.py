from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
import random


def load_patients(ndjson_path: str):
    patients = []
    with open(ndjson_path, "rt") as f:
        for line in f:
            bundle = Bundle.parse_raw(line.strip("\n"))
            patient_entry = next(filter(lambda e: e.resource.resource_type == "Patient", bundle.entry))
            patients.append(patient_entry.resource)
    return patients


_patients = load_patients("versicherte.fhir.ndjson")


def pick_patient() -> Patient:
    return random.choice(_patients)