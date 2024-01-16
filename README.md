## Description

> This repository contains a Flask web application that provides user voting on dogs and cats. The application is containerized using Docker, and it can be tested with a PostgreSQL database using Docker Compose.

## Prerequisites

Before you begin, make sure that Docker installed on your machine.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Adhaammohammed/DevOps-Exercise.git
    ```

2. Navigate to the app directory:

    ```bash
    cd DevOps-Exercise/TASK3
    ```
    
3. Build the Docker image:

    ```bash
    docker build -t .
    ```

## Usage

To test the application and PostgreSQL database, use Docker Compose:

```bash
docker-compose build
docker-compose up
```
Access the application in your browser at http://localhost:5005 or 0.0.0.0:5005.

