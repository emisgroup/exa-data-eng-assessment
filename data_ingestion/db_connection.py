from sqlalchemy import create_engine

print('run this command to get the postgres IP `docker inspect postgres_container_emis | grep "IPAddress"`')
ip = input()
if ip:
    db_conn = create_engine(f"postgresql+psycopg2://admin1:password@{ip}:5432/fhir")
else:
    exit()
