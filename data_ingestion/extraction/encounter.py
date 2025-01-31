def ingest_encounter_data(data):
    id = data.get('id')
    status = data.get('status')
    class_code = data.get('class')['code']
    type_code = data.get('type')[0]['coding'][0]['code']
    type_text = data.get('type')[0]['coding'][0]['display']
    subject = data.get('subject')['reference'].split(':')[-1]
    start_date = data.get('period')['start']
    end_date = data.get('period')['end']
    location = data.get('location')[0]['location']['display']
    serviceprovider = data.get('serviceProvider')['display']
    return (id, status, class_code, type_code, type_text, subject, start_date, end_date, location, serviceprovider)
