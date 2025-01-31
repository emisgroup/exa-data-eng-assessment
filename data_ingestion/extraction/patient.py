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