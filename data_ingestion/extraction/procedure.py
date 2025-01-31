def ingest_procedure_data(data):
    id = data.get('id', '')
    status = data.get('status', '')
    code = [each['code'] for each in data.get('code', {}).get('coding', [])]
    text = [each['display'] for each in data.get('code', {}).get('coding', [])]
    subject = data.get('subject', {}).get('reference', '').split(':')[-1]
    encounter = data.get('encounter', {}).get('reference', '').split(':')[-1]
    performed_start_date = data.get('performedDateTime', {}).get('start', '')
    performed_end_date = data.get('performedPeriod', {}).get('end', '')
    location = data.get('location', {}).get('display', '')
    return (id, status, code, text, subject, encounter, performed_start_date, performed_end_date, location)
