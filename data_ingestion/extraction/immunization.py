def ingest_immunization_data(data):
    id = data.get('id')
    status = data.get('status')
    vaccine_code = [each['code'] for each in data.get('vaccineCode')['coding']]
    vaccine_name = [each['display'] for each in data.get('vaccineCode')['coding']]
    patient = data['patient']['reference'].split(':')[-1]
    encounter = data['encounter']['reference'].split(':')[-1]
    occurrenceDateTime = data.get('occurrenceDateTime')
    primary_source = data.get('primarySource')
    location = data.get('location')['display']
    return (id, status, vaccine_code, vaccine_name, patient, encounter, occurrenceDateTime, primary_source, location)
