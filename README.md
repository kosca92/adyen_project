## Table of contents
* [General info](#general-info)
* [Technical info](#technical-info)
* [Setup](#setup)
* [Production Setup](#production-setup)

## General info
Adyen Case Study: Create a service that calculates the current balance of each user once per minute, and writes the balance to the `balance` table. \
For more detail read the attached document [here](Moss/DE_case_study.pdf).

	
## Technical info
For this project a **Docker** is used, so you do not have to worry about environment management. 
**Docker** is a _containerization software_ that allows to isolate software in a similar way to virtual machines.


In total three **containers** are created: 
* **Postgres**: free and open-source relational database management system
* **Airflow**: web-based GUI tool used to interact with the Postgres database
* **Scheduler**: job scheduler to automate the `script.py` to run every minute

For both **Postgres** and **pgAdmin** containers I used the pre-configured Docker Images. The third **Cronjob** container is created based on Python image with additional cronjob service.
**Docker Compose** is used for configuring and starting multiple Docker containers on the same host–so you don’t have to start each container separately. With a single command `docker-compose up` you create and start all the services from your configuration. 

	
## Setup
To run this project do following steps
1. 	Clone the repository and run  `docker-compose up`. 
2. 	Open the **Airflow** on your localhost, and use the following as your login credentials:
		e-mail: `admin@admin.com`
		pw: `root`
3. 	Click on `Add New Server` and use the following credentials: 
		General>> 		Name: `airflow`
		Connection>> 	Host name/adress: `airflow`
	  					Username: `airflow`
						pw: `airflow`

