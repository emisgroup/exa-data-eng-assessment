Run PostgreSQL in a Docker container:

    docker run -d \
    --name postgres_container_emis \
    -e POSTGRES_USER=admin1 \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=fhir \
    -p 5432:5432 \
    -v pgdata:/var/lib/postgresql1/data \
    postgres:latest

Start the PostgreSQL container :

    docker start postgres_container_emis

Build the Docker image for FHIR ingestion:

    docker build -t fhir_ingestion .

Run the FHIR ingestion container:

    docker run -t fhir_ingestion

Provide the PostgreSQL container's IP address when prompted:

    <input_ip_address_of_postgres_container_emis>
