def ingest_eob_data(data):
    id = data.get('id')
    status = data.get('status')
    patient = data['patient']['reference'].split(':')[-1]
    insurer = data['insurer']['display']
    claim_id = data['claim']['reference'].split(':')[-1]
    total_amount = float(data['total'][0]['amount']['value'])
    payment_amount = float(data['payment']['amount']['value'])
    return (id, status, patient, insurer, claim_id, total_amount, payment_amount)
