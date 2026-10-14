# DevOps Practice Website

A simple website built with Python and Docker for practising Git, GitHub, and DevOps fundamentals.

## Features

- Simple HTML website
- Python HTTP server
- Docker container deployment
- Port mapping for local access

## Technologies

- Python 3.11
- Docker
- Git
- GitHub

## Run Locally

Make sure Python is installed, then run:

```powershell
python app.py
```

Open http://localhost:5000 in your browser.

## Run with Docker

Build the Docker image:

```powershell
docker build -t devops-practice .
```

Start the container:

```powershell
docker run -d --name devops-website -p 8080:5000 devops-practice
```

Open http://localhost:8080 in your browser.

## Git Practice

This project is used to practise commits, branches, pushes, and pull requests.
