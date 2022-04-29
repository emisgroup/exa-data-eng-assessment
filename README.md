# Data Engineer - Technical Assesment
Our tech teams are curious, driven, intelligent, pragmatic, collaborative and open-minded and you should be too. 

## Testing Goals
We are testing your ability to design and prototype a scalable data-pipeline (with code) underpinned with good data/software engineering principles from a blank canvas. You will need to use your intellect, creativity, judgement and be comfortable making decisions to produce a solution. 

You will have approximately 1 week to complete this task but can as much or as little time as you deem necessary to **demonstrate your understanding of the problem, your range of skills and approach to problem solving**.

Some successful candidates have spent as little as 3 hours whilst others have used the full week because they've enjoyed exploring different ideas, technologies and approaches. 

## The Task
An external system / supplier is sending patient data to our platform using the FHIR standard. Our analytics teams find this format difficult to work with when creating dashboards and visualizations. You are required to tranform these FHIR messages into a more workable format preferably in a tabular format. Include any documentation / commentary you deem necessary.


## The Solution
If you are applying for a position that uses one specific programming language, please write your solution in that language, otherwise your solution can use any of the following technologies along with **any frameworks, libraries you feel appropriate**:

- **Programming Languages** - Java / Python / Scala / Go / C#
- **Data Storage Layer** - MongoDB / MySql / Postgres / SQLServer Express / Filesystem (CSV/Parquet/Orc)

Containerising your pipeline using docker / docker-compose is strongly encouraged, but not required.

## Evaluation
We take into account 5 areas when evaluating a solution. Each criteria is evaluated from 0 (non-existent) to 5 (excellent) and your final score would be a simple average across all 5 areas. These are:

- **Functionality**: Is the solution correct? Does it run in a decent amount of time? How well thought and architected is the solution?
- **Good Practices**: Does the code follow standard practices for the language and framework used? Take into account reusability, names, function length, structure, how crendentials are handled, etc.
- **Testing**: Unit and integration tests.
- **Execution environment**: Container, Virtual Environment, Dependency Management, Isolation, Ease of transition into a production environment etc.
- **Documentation**: How to install and run the solution? How to see and use the results? What is the architecture? Any next steps?

## Context
[FHIR](/https://www.hl7.org/fhir/overview.html) is a popular standard within healthcare used by healthcare systems to exchange data and represent details of paitents in a standardised way. Some sample FHIR data has been generated in the data directory using a tool called [synthea](https://www.hl7.org/fhir/overview.html). 

## Submit your solution	
Create a public Github repository and push your solution including any documentation you feel necessary. Commit often - we would rather see a history of trial and error than a single monolithic push. When you're finished, please send us the URL to the repository. 
