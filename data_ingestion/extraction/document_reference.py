def ingest_document_reference(data):
    id = data.get('id')
    status = data.get('status')
    type = [{'code': each['code'], 'display': each['display']} for each in data.get('type')['coding']]
    category = [{'code': each['code'], 'display': each['display']} for each in data.get('category')[0]['coding']]
    subject = data['subject']['reference'].split(':')[-1]
    date = data.get('date')
    author = data.get('author')[0]['display'].split(':')[-1]
    custodian = data.get('custodian')['display'].split(':')[-1]
    encounter = data['context']['encounter'][0]['reference'].split(':')[-1] 
    period_start = data['context']['period']['start']
    period_end = data['context']['period']['end']
    return (id, status, type, category, subject, date, author, custodian, encounter, period_start, period_end)
