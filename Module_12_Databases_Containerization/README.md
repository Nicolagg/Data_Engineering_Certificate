# Module 12 Databases Containerization

## Abstract
The goal of the assignment is to impart hands-on expertise in database management, containerization technologies, and cloud-based systems.

**Part 1** involves setting up and initializing a MySQL database. This database is created within a Docker container configured to operate on port 3300.

Below are the Python scripts created to interact with the MySQL database:
- [create.py](https://github.com/Nicolagg/Data_Engineering_Certificate/blob/main/Module_12_Databases_Containerization/Part%201/create.py)
- [driver.py](https://github.com/Nicolagg/Data_Engineering_Certificate/blob/main/Module_12_Databases_Containerization/Part%201/driver.py)
- [insert.py](https://github.com/Nicolagg/Data_Engineering_Certificate/blob/main/Module_12_Databases_Containerization/Part%201/insert.py)
- [selects.py](https://github.com/Nicolagg/Data_Engineering_Certificate/blob/main/Module_12_Databases_Containerization/Part%201/selects.py)
  
**Part 2** focuses on using MongoDB, with the database running within a Docker container on port 27017. Interaction with the database is facilitated through Python scripts that exercise functionalities such as adding employees in JSON format, filtering records based on specific attributes, updating existing records, and deleting them.

Below are the Python scripts created to interact with the MongoDB database:
- [mongoDBCreate.py](part%202/mongoDBFindOne.py)
- [mongoDBDeleteMany.py](part%202/mongoDBDeleteMany.py)
- [mongoDBDeleteOne.py](part%202/mongoDBDeleteOne.py)
- [mongoDBFindMany.py](part%202/mongoDBFindMany.py)
- [mongoDBFindOne.py](part%202/mongoDBFindOne.py)
- [mongoDBUpdateMany.py](part%202/mongoDBUpdateMany.py)
- [mongoDBUpdateOne.py](part%202/mongoDBUpdateOne.py)
- [read.py](part%202/read.py)
- [write.py](part%202/write.py)

**Part 3** shifts focus to the Redis database management system. A new Docker container is specifically set up for Redis and is exposed on port 6379. Python scripts are used to write data into, and read data from, this containerized Redis database using Redis-specific methods like mset and get.

Below are the Python scripts created to interact with the Redis database:
- [read.py](Part%203/read.py)
- [write.py](Part%203/write.py)
  
**Part 4** extends the exercise to the cloud using Firebase, where a real-time database is established. This Firebase database is also encapsulated within a Docker container. Permissions for Python-scripted read and write operations are configured, and the database is populated with two custom entries, one of which contains an additional field. Command-line executions are used at each stage to verify the steps.

Below is the Python script created to interact with the Firebase database:
- [fire.py](Part%204/fire.py)

---
**[🔙 Back to portfolio](https://nicolagg.github.io/)**
