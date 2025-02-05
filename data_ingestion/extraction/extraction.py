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

def ingest_eob_data(data):

    id = data.get('id')
    status = data.get('status')
    patient = data['patient']['reference'].split(':')[-1]
    insurer = data['insurer']['display']
    claim_id = data['claim']['reference'].split(':')[-1]
    total_amount = float(data['total'][0]['amount']['value'])
    payment_amount = float(data['payment']['amount']['value'])
    return (id, status, patient, insurer, claim_id, total_amount, payment_amount)

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

def ingest_patient_data(data):

    id = data.get('id')
    identifier = data.get('identifier')
    ppn, dl, ss, mr = None, None, None, None
    for each in identifier:
        if 'type' in each:
            if 'coding' in each['type']:
                for each_coding in each['type']['coding']:
                    if each_coding['code'] == 'PPN':
                        ppn = each['value']
                    if each_coding['code'] == 'DL':
                        dl = each['value']
                    if each_coding['code'] == 'SS':
                        ss = each['value']
                    if each_coding['code'] == 'MR':
                        mr = each['value']
    
    name =  data.get('name')[0]['given'][0] + ' ' + data.get('name')[0]['family']
    telecom = data.get('telecom')[0]['value']
    gender = data.get('gender')
    birthDate = data.get('birthDate')
    deceasedDateTime = data.get('deceasedDateTime', '')
    address = data.get('address')[0]['line'][0]+ ', ' + data.get('address')[0]['city'] + ', '+ data.get('address')[0]['state'] +', '+ data.get('address')[0]['country']
    maritalStatus = data.get('maritalStatus')['coding'][0]['code']
    communication = data.get('communication')[0]['language']['text']
    return (id, ppn, dl, ss, mr, name, telecom, gender, birthDate, deceasedDateTime, address, maritalStatus, communication)

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
