# 🌐 Uptime Monitor

A lightweight full-stack uptime monitoring application built with **FastAPI**, **React**, **SQLite**, and **Docker**. The application periodically checks registered URLs, records their health status, response time, HTTP status code, and timestamp, and displays the latest results on a live dashboard.

---

## Features

* Register URLs to monitor
* Automatic background health checks
* Stores:

  * HTTP Status Code
  * Response Time
  * Timestamp
* Detects whether a website is **UP** or **DOWN**
* Live dashboard with automatic refresh
* Dockerized backend and frontend
* Launch the complete application with a single Docker command

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* APScheduler
* Uvicorn

### Frontend

* React
* Vite
* Axios

### DevOps

* Docker
* Docker Compose
* Nginx

---

# Project Structure

```text
uptime-monitor/
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   └── .env
│
├── docker-compose.yml
├── README.md
└── AI_LOG.md
```

---

# Setup

## Prerequisites

* Docker Desktop
* Docker Compose

---

## Run the Application

From the project root directory:

```bash
docker compose up --build
```

---

## Access the Application

Frontend

```text
http://localhost:5173
```

Backend API

```text
http://localhost:8000
```

Swagger Documentation

```text
http://localhost:8000/docs
```

---

# Testing Instructions

## Step 1

Open the frontend dashboard:

```text
http://localhost:5173
```

---

## Step 2

Add a healthy URL.

Example:

```text
https://example.com
```

Expected Result:

* Status: **UP**
* HTTP Status Code: **200**
* Response Time displayed
* Last Checked timestamp updated

---

## Step 3

Add an invalid URL.

Example:

```text
https://this-url-does-not-exist-123456789.com
```

Expected Result:

* Status: **DOWN**
* Status Code unavailable
* Response Time unavailable
* Error handled gracefully

---

## Step 4

Wait for the scheduler to run (approximately every minute).

Verify that:

* The dashboard refreshes automatically.
* Response times are updated.
* Status changes are reflected in the UI.

---

# API Endpoints

| Method | Endpoint | Description                 |
| ------ | -------- | --------------------------- |
| GET    | `/`      | Health check                |
| GET    | `/urls`  | Retrieve all monitored URLs |
| POST   | `/urls`  | Register a new URL          |

---

# How It Works

1. User registers a URL from the frontend.
2. FastAPI stores the URL in SQLite.
3. APScheduler periodically checks every registered URL.
4. Each check stores:

   * Status
   * Status Code
   * Response Time
   * Timestamp
5. The React dashboard polls the backend periodically and displays the latest status.

---

# Deployment Sketch

For a production deployment, this application can be hosted on any cloud provider such as AWS, Azure, or Google Cloud.

A simple deployment architecture would be:

```text
Internet
      │
      ▼
Load Balancer
      │
      ▼
Docker Host (EC2 / VM)
      │
      ├── Frontend (Nginx + React)
      └── Backend (FastAPI)
              │
              ▼
         SQLite Database
```

Deployment Steps:

1. Provision a virtual machine.
2. Install Docker and Docker Compose.
3. Clone the repository.
4. Run:

```bash
docker compose up -d --build
```

5. Expose ports 80 and 8000 (or configure a reverse proxy such as Nginx).

---

# Future Improvements

* Authentication
* Email/Slack notifications
* Historical uptime analytics
* PostgreSQL support
* URL deletion and editing
* Charts and uptime statistics
* Kubernetes deployment
* HTTPS with reverse proxy

---

# Author

**Anusha Dixit**
