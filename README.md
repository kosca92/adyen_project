## Table of contents
* [General info](#general-info)
* [Technical info](#technical-info)
* [Setup](#setup)


## General info
Adyen Case Study: Create a service that... (this link does not work yet [here](Adyen/case_study.pdf).)

	
## Technical info
For this project a **Docker** is used, so you do not have to worry about environment management. 
**Docker** is a _containerization software_ that allows to isolate software in a similar way to virtual machines.


In total three **containers** are created: 
* **Postgres**: free and open-source relational database management system
* **Airflow**: web-based GUI tool that lets you build and run workflows (...explain Dag etc)
* **Cronjob**: Creates Jobs on a repeating  schedule

For both **Postgres** and **Airflow** containers I used the pre-configured Docker Images. The third **Cronjob** container is created based on Python image with additional cronjob service.
**Docker Compose** is used for configuring and starting multiple Docker containers on the same host–so you don’t have to start each container separately. With a single command `docker-compose up` you create and start all the services from your configuration. 

In the **Postgres** instance we  have 3 databases: 
* Airflow_db:  saves the metadata from Airflow to the db,  i.e. Dag's metadata, etc (caro you need to learn more about this)
* Terminal_db: holds the fake terminal data (Also the cronjob replaces/updates it)
* Results_db: this will hold the result table of the DAG


## Setup
To run this project do following steps
1. 	Clone the repository and run  `docker-compose up`. 
2. 	Open the **Airflow** on your localhost, and use the following as your login credentials:
		e-mail: `admin`
		pw: `admin1234`
3. 	Click on `Admin`, then `Connections` and add the connections to your 3 databases:
        * add this stuff later [todo] 
      
      Host name/adress: `airflow`
                          Username: `airflow`
                        pw: `airflow`

