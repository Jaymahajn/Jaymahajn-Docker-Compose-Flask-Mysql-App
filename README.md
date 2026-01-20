Flask + MySQL using Docker Compose

This project demonstrates a basic Flask web application connected to a MySQL database, fully containerized using Docker and Docker Compose.

The goal of this project is to understand:

Docker containers

Docker Compose services

Flask ↔ MySQL connection

Service names vs container names

Basic data storage using MySQL

Tech Stack

Python 3.11

Flask

MySQL 8

Docker

Docker Compose

Project Structure
Docker-Flask-SQL-Project/
│
├── app.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── templates/
    └── index.html

Application Overview

The Flask app displays a simple HTML form with a text input.

When the user submits text, it is stored in a MySQL database.

Flask creates the required table automatically if it does not exist.

MySQL runs in a separate container managed by Docker Compose.

Both containers communicate using a Docker network.

Docker Compose Services
1️⃣ MySQL Service (sql)

Image: mysql:8

Database name: testdb

Username: root

Password: root

Container name: sql-host

2️⃣ Flask Service (web)

Built using a custom Dockerfile

Runs on port 5000

Container name: flask-app

Connects to MySQL using environment variables

Important Concept: Service Name vs Container Name

Service name: sql

Container name: sql-host

Inside Docker Compose, services communicate using the service name, not the container name.

That is why Flask uses:

MYSQL_HOST=sql

How to Run the Project
1️⃣ Clone the repository
git clone <your-repository-url>
cd Docker-Flask-SQL-Project

2️⃣ Start the containers
docker-compose up -d

3️⃣ Verify running containers
docker ps


You should see:

sql-host

flask-app

4️⃣ Open the application

Visit in your browser:

http://localhost:5000

Environment Variables Used
Variable	Description
MYSQL_HOST	MySQL service name (sql)
MYSQL_USER	Database username
MYSQL_PASSWORD	Database password
MYSQL_DATABASE	Database name
Database Behavior

The database must already exist (testdb)

Flask creates the table automatically:

messages (id, text)


Each form submission inserts a new row into the table

Files Description
app.py

Flask application logic

Connects to MySQL

Creates table if not present

Handles form submission

docker-compose.yml

Defines Flask and MySQL services

Creates a custom Docker network

Dockerfile

Builds the Flask application image

Installs dependencies

Runs the Flask app

requirements.txt

Lists Python dependencies

index.html

Simple HTML form to submit text

Learning Outcome

By completing this project, you learn:

How Docker Compose works

How services communicate in Docker

How Flask connects to MySQL

How environment variables are used in containers

How small YAML mistakes can break deployments

Author

Jay Mahajan

