# Flask + MySQL Docker App

A simple Flask web application that allows users to submit text messages and stores them in a MySQL database using Docker.

## Features

- Submit text messages through a web form
- Messages are stored in a MySQL database
- Fully containerized using Docker

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/) (optional, but recommended)

## Project Structure

.
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
└── README.md

## Setup Instructions

### 1. Create a Docker network (optional)
```bash
docker network create flask-mysql-network

2. Run MySQL container
docker run -d \
  --name mysql \
  --network flask-mysql-network \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=testdb \
  -v mysql-data:/var/lib/mysql \
  mysql:8


3. Build and run Flask container
docker build -t flask-mysql-app .
docker run -d \
  --name flask-app \
  --network flask-mysql-network \
  -p 5000:5000 \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=root \
  -e MYSQL_DATABASE=testdb \
  flask-mysql-app


4. Access the app
Open your browser and go to: http://localhost:5000


Notes

The app automatically creates the messages table if it doesn't exist.

Data is persisted using a Docker volume mysql-data.

Requirements

Listed in requirements.txt:

Flask
mysql-connector-python
