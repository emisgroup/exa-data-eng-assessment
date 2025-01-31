def ingest_condition_data(data):
    id = data.get('id')
    clinical_status = data.get('clinicalStatus')['coding'][0]['code']
    verification_status = data.get('verificationStatus')['coding'][0]['code']
    category_code = data.get('category')[0]['coding'][0]['code']
    category = data.get('category')[0]['coding'][0]['display']
    subject = data['subject']['reference'].split(':')[-1]
    encounter = data['encounter']['reference'].split(':')[-1]
    onsetrecorded = data.get('onsetDateTime')
    recorded_date = data.get('recordedDate')
    code = data.get('code')['coding'][0]['code']
    text = data.get('code')['coding'][0]['display']
    return (id, clinical_status, verification_status, category_code, category, subject, encounter, onsetrecorded, recorded_date, code, text) 
