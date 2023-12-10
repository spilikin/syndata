from fhir.resources.bundle import Bundle
import random


def load_organizations(ndjson_path: str):
    orgs = []
    with open(ndjson_path, "rt") as f:
        for line in f:
            bundle = Bundle.parse_raw(line.strip("\n"))
            orgs.append(bundle)
    return orgs


_organizations = load_organizations("arztpraxen.fhir.ndjson")


def pick_organization() -> Bundle:
    return random.choice(_organizations)
