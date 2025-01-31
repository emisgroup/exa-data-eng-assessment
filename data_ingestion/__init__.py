import pandas as pd
import json, glob
from extraction.claim import *
from extraction.condition import *
from extraction.diagnostic import *
from extraction.document_reference import *
from extraction.encounter import *
from extraction.explanation_of_benefit import *
from extraction.immunization import *
from extraction.patient import *
from extraction.procedure import *

patient_data = []
encounter_data = []
condition_data = []
diagnostic_data = []
document_reference = []
claim_data = []
procedure_data = []
immunization_data = []
eob_data = []

json_files = glob.glob("../data/*.json")
for file in json_files:
    with open(file, 'r') as f:
        raw_data = json.load(f) 

    for each_entry in raw_data['entry']:
        if each_entry['resource']['resourceType'] == 'Patient':
            patient_data.append(ingest_patient_data(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'Encounter':
            encounter_data.append(ingest_encounter_data(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'Condition':
            condition_data.append(ingest_condition_data(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'DiagnosticReport':
            diagnostic_data.append(ingest_diagnostic_data(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'DocumentReference':
            document_reference.append(ingest_document_reference(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'Claim':
            claim_data.append(ingest_claim_data(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'Procedure':
            procedure_data.append(ingest_procedure_data(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'Immunization':
            immunization_data.append(ingest_immunization_data(each_entry['resource']))
        if each_entry['resource']['resourceType'] == 'ExplanationOfBenefit':
            eob_data.append(ingest_eob_data(each_entry['resource']))

# Write Dataframes into any external storage systems.Here I'm writing into CSV files 
pd.DataFrame(patient_data, columns=['id', 'passport_no', 'driving_license', 'social_security_no', 'medical_record_no', 'name', 'telecom', 'gender', 'birth_date', 'deceased_date_time', 'address', 'marital_status', 'communication']).to_csv('output/patient_data.csv', index=False, sep=';')
pd.DataFrame(encounter_data, columns=['id', 'status', 'class_code', 'type_code', 'type_text', 'subject', 'start_date', 'end_date', 'location', 'service_provider']).to_csv('output/encounter_data.csv', index=False, sep=';')
pd.DataFrame(condition_data, columns=['id', 'clinical_status', 'verification_status', 'category_code', 'category', 'subject', 'encounter', 'onset_recorded', 'recorded_date', 'code', 'text']).to_csv('output/condition_data.csv', index=False, sep=';')
pd.DataFrame(diagnostic_data, columns=['id', 'status', 'category', 'subject', 'encounter', 'effective_date', 'issued_date', 'performer']).to_csv('output/diagnostic_data.csv', index=False, sep=';')
pd.DataFrame(document_reference, columns=['id', 'status', 'type', 'category', 'subject', 'date', 'author', 'custodian', 'encounter', 'period_start', 'period_end']).to_csv('output/document_reference.csv', index=False, sep=';')
pd.DataFrame(claim_data, columns=['id', 'status', 'type_code', 'patient', 'billable_start_date', 'billable_end_date', 'created_date', 'provider', 'priority', 'insurence', 'service_codes', 'total_amount']).to_csv('output/claim_data.csv', index=False, sep=';')
pd.DataFrame(procedure_data, columns=['id', 'status', 'code', 'text', 'subject', 'encounter', 'performed_start_date', 'performed_end_date', 'location']).to_csv('output/procedure_data.csv', index=False, sep=';')
pd.DataFrame(immunization_data, columns=['id', 'status', 'vaccine_code', 'vaccine_name', 'patient', 'encounter', 'occurrence_date_time', 'primary_source', 'location']).to_csv('output/immunization_data.csv', index=False, sep=';')
pd.DataFrame(eob_data, columns=['id', 'status', 'patient', 'insurer', 'claim_id', 'total_amount', 'payment_amount']).to_csv('output/eob_data.csv', index=False, sep=';')
