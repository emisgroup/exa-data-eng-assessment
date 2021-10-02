# Data Engineer - Technical Assesment
Our tech teams are curious, driven, intelligent, pragmatic, collaborative and open-minded and you should be too.
## Testing Goals
We are testing your ability to design and prototype a scalable data-pipeline (with code) underpinned with good data/software engineering principles. 

## The Task
An external system / supplier is sending patient data to our platform using the FHIR standard. Our analytics teams find this format difficult to work with when creating dashboards and visualizations. You are required to tranform these FHIR messages into a more workable format preferably in a tabular format.

You will have approximately 1 week to complete this task and should focus on an MVP but you are free to take this as far as you wish.

## The Solution
Your pipeline can use any of the following technologies along with **any frameworks, libraries you feel appropriate**:

- **Programming Languages** - Java / Python / Scala 
- **Data Storage Layer** - MongoDB / MySql / Postgres / SQLServer Express / Filesystem (CSV/Parquet/Orc)

You should containerise your pipeline using docker / docker-compose.

## Context
[FHIR](/https://www.hl7.org/fhir/overview.html) is a popular standard within healthcare used by healthcare systems to exchange data and represent details of paitents in a standardised way. Some sample FHIR data has been generated in the data directory using a tool called [synthea](https://www.hl7.org/fhir/overview.html). 

## Submit your solution	
Create a public Github repository and push your solution including any documentation you feel necessary. Commit often - we would rather see a history of trial and error than a single monolithic push. When you're finished, please send us the URL to the repository. 
