# Modul 16: Real-Time Bus Tracking Web Application with Data Analysis
## Abstract: 
In this project, we enhanced an existing web application prototype, initially developed to display hardcoded positions of buses along MBTA Route 1 using Mapbox. The main objectives were to add real-time tracking and data analysis features. We integrated a MySQL database running in a Docker container to store real-time data fetched from the MBTA API every 10 seconds. The application then performed Change Data Capture (CDC) on MySQL, propagating any changes to a MongoDB database for further analysis.

The project was divided into two main submissions. The first consisted of a Word document detailing the development process with relevant screenshots, adhering to the guidelines set in the Project 16.1 Rubric. The second was a Jupyter Notebook that analyzed the stored data to answer key performance questions.

Data Analysis Results:

Calculated the average time taken for a bus to complete Route 1.
Provided a plot-type visualization to represent various metrics.
Estimated bus speed between the first and last stops using the Haversine formula for distance calculation.
The architecture utilized Docker containers networked together under a custom network, "MBTANetwork," and included components such as a Flask web server and a Debezium CDC monitor. This project serves as a comprehensive example of building a scalable, real-time data tracking and analysis solution.

## Go to the project

[Jupyter Notebook](https://github.com/Nicolagg/Data_Engineering_Certificate/blob/main/Modul_16_Real-Time_Bus_Tracking_Web_Application/Module16%20final.ipynb)

[Mysql Docker repository](https://github.com/Nicolagg/Data_Engineering_Certificate/tree/main/Modul_16_Real-Time_Bus_Tracking_Web_Application/mysqlDocker)

[Flask repository](https://github.com/Nicolagg/Data_Engineering_Certificate/tree/main/Modul_16_Real-Time_Bus_Tracking_Web_Application/Module16ProjectFlask)

[Full repository](https://github.com/Nicolagg/Data_Engineering_Certificate/tree/main/Modul_16_Real-Time_Bus_Tracking_Web_Application)


---

**[🔙 Back to portfolio](https://nicolagg.github.io/)**
