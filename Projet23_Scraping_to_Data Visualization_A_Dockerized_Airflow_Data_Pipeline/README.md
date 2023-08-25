# Creating a Sensemaking Data Pipeline
## Abstract
This project aims to execute a comprehensive data analysis workflow to extract, clean, analyze, and visualize course titles from MIT's course catalog. Leveraging Python's urllib library, the project begins by scraping unstructured data from the web. The data is then cleaned and structured using Python's Beautiful Soup library and stored in JSON format. A suite of text analytics techniques are applied to count the frequency of words in course titles. All these steps are orchestrated using Apache Airflow, encapsulated within a Docker container for ease of deployment and scalability. The final output is a visually compelling web application utilizing the D3.js library to represent the word frequency in MIT course titles.

The project is structured into two major parts:

### Part 1: Code Development
The first part focuses on developing the codebase. Several Python functions are defined, each performing specific tasks, from data pulling to cleaning to analytics. These Python functions are organized into an Airflow DAG to automate the workflow. The project comprises tasks such as importing libraries, defining Python functions (catalog(), combine(), titles(), clean(), count_words()), and setting up the Airflow pipeline with a total of six tasks.

### Part 2: Code Execution
The second part emphasizes executing the codebase in a Dockerized environment. It starts by copying the Python code into the appropriate Airflow directory in the Docker container. Resources are allocated via the Docker UI to optimize computational efficiency. Airflow, within Docker, is then used to execute the pipeline. The resultant dataset, a JSON file containing word frequencies, is then converted into a .js file. Finally, the data is visualized in a browser using D3.js-based bubble charts.

With the end-to-end workflow accommodating around 1,391,580 rows of data, the project serves as a comprehensive guide on how to orchestrate a complex data analytics pipeline using modern tools like Python, Apache Airflow, and Docker.

## Go to the project

[Assignment submission](assignment_submission.md)  
[Python code](assignment.py)
