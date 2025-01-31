def ingest_diagnostic_data(data):
    id = data.get('id')
    status = data.get('status')
    category = [{'code': each['code'], 'display': each['display']} for each in data.get('category')[0]['coding']]
    subject = data['subject']['reference'].split(':')[-1]
    encounter = data['encounter']['reference'].split(':')[-1]
    effective_date = data.get('effectiveDateTime')
    issued_date = data.get('issued')
    performer = data.get('performer')[0]['display']
    return (id, status, category, subject, encounter, effective_date, issued_date, performer)
