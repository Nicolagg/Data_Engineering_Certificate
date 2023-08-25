# Module 19: Processing Big Data with Spark and Airflow
## Abstract
This assignment serves as a comprehensive demonstration of in PySpark and Apache Airflow.

Part 1: PySpark
In the first section, the assignment kicked off with the setting up of a Docker container based on the Bitnami Spark Docker image. A particularly large dataset, "departuredelays.csv," containing 1,391,580 rows, was chosen for analysis to simulate real-world complexity. The container was initialized successfully, and the data file was imported. A variety of PySpark functionalities were employed, including initiating a PySpark session, loading the large CSV data into a dataframe, and running SQL queries for data analysis. Two specific SQL queries were executed: one to identify the first 15 flights from Philadelphia to Dallas Fort Worth with a delay exceeding 150 minutes, and another to pinpoint the first 10 flights with a distance less than 200 miles and another set of flights with a distance greater than 600 miles.

Part 2: Airflow
The latter part transitioned the focus to Apache Airflow, an automation tool used for defining tasks and dependencies in programmable workflows. The environment was initialized using Docker containers, where a Directed Acyclic Graph (DAG) was created. This DAG contained a Python function designed to square a number and was structured to execute this function as a task in the Airflow workflow. Environment configurations were set up to ensure the smooth execution of the DAG.

## Go to the project

[Assignment submission](assignment_submission.md)


---
**[🔙 Back to portfolio](https://nicolagg.github.io/)**
