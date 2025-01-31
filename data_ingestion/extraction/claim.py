def ingest_claim_data(data):
    id = data.get('id')
    status = data.get('status')
    type_code = data.get('type')['coding'][0]['code']
    patient = data['patient']['reference'].split(':')[-1]
    billable_start_date = data.get('billablePeriod')['start']
    billable_end_date = data.get('billablePeriod')['end']
    created_date = data.get('created')
    provider = data['provider']['display']
    priority = data.get('priority')['coding'][0]['code']
    # diagnosis_reference = [ each.get('diagnosisReference').get('reference') for each in data.get('diagnosis', []) if each  != None]
    insurence = [each['coverage']['display'] for each in data.get('insurance')]
    service_codes =  [each['productOrService']['coding'][0]['code'] for each in data['item']]
    total_amnt = float(data.get('total')['value'])
    return (id, status, type_code, patient, billable_start_date, billable_end_date, created_date, provider, priority, insurence, service_codes, total_amnt)
