# Performing ETL Using NiFi
## Abstract
The assignment is about the ETL (Extract, Transform, Load) process operations using Apache NiFi, a data integration tool, on a dataset of movies. Divided into two parts, the assignment first focuses on creating a NiFi pipeline to transfer data from an Excel file (.xlsx) to a Comma-Separated Values (CSV) file. The second part extends the ETL process to transfer this CSV data into a MySQL database. The assignment will be conducted within a Docker environment to instantiate NiFi and MySQL containers connected to the same network, facilitating the ETL process.

The first part requires configuring three key NiFi processors: GetFile, ConvertExcelToCSVProcessor, and PutFile. We must configure these processors to read an Excel file, convert it to CSV format, and save it. The second part is more complex, involving a five-step pipeline in NiFi consisting of GetFile, SplitText, ConvertRecord, ConvertJSONToSQL, and PutSQL processors. These processors collaborate to read a CSV file, transform the data, and populate it into a MySQL database.

## Go to the project

[Raw Data (Excel file)](movies.xlsx)

[Output Data (CSV)](movies.csv)

[Assignment submission](assignment_submission.md)

---
**[🔙 Back to portfolio](https://nicolagg.github.io/)**

