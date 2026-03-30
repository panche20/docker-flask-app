# 🚀 URL Shortener Microservice (Dockerized)

A production-style **URL Shortener service** built using **FastAPI, Redis, and Nginx**, fully containerized with **Docker & Docker Compose**.

---

## 📌 Project Overview

This project demonstrates a **multi-container microservice architecture**:

* 🔹 **Nginx** → Reverse proxy (handles incoming traffic)
* 🔹 **FastAPI App** → URL shortening + analytics
* 🔹 **Redis** → Persistent storage for URL mappings & click counts

---

## 🏗️ Architecture

```
Client → Nginx → FastAPI → Redis
```

* Nginx routes requests to the FastAPI service
* FastAPI handles business logic
* Redis stores URL mappings and click data

---

## 📂 Project Structure

```
url-shortener/
├── app/                     # FastAPI application
│   ├── main.py
│   └── requirements.txt
├── nginx/                  # Nginx reverse proxy config
│   └── nginx.conf
├── Dockerfile              # Multi-stage build
├── docker-compose.yml      # Production setup
├── docker-compose.override.yml  # Dev overrides
├── .env                    # Environment variables
└── .dockerignore
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI (Python)
* **Cache/DB:** Redis
* **Reverse Proxy:** Nginx
* **Containerization:** Docker, Docker Compose
* **Architecture:** Microservices (3-tier)

---

## 🔐 Environment Variables

Create a `.env` file:

```
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=strongpassword123
APP_PORT=8000
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2️⃣ Start services

```bash
docker-compose up --build
```

### 3️⃣ Access application

* App: http://localhost
* Docs: http://localhost/docs
* Health: http://localhost/health

---

## 🔗 API Endpoints

### ➤ Create Short URL

```bash
POST /shorten
```

Request:

```json
{
  "url": "https://example.com"
}
```

Response:

```json
{
  "short_code": "abc123",
  "short_url": "/r/abc123"
}
```

---

### ➤ Redirect

```
GET /r/{code}
```

---

### ➤ Get Stats

```
GET /stats/{code}
```

Response:

```json
{
  "short_code": "abc123",
  "url": "https://example.com",
  "clicks": 5
}
```

---

### ➤ Health Check

```
GET /health
```

---

## 🐳 Docker Highlights

* ✅ Multi-stage Docker build (optimized image size)
* ✅ Non-root user for security
* ✅ Service health checks
* ✅ Persistent Redis volume
* ✅ Environment-based configuration

---

## 🔄 Development Mode

Use override file:

```bash
docker-compose up --build
```

Features:

* Hot reload enabled (`--reload`)
* Local code mounted as volume

---

## 📊 Key Features

* URL shortening with unique codes
* Click tracking & analytics
* Redis-based fast storage
* Reverse proxy with Nginx
* Health monitoring for services
* Production-ready container setup

---

## 🧠 Learnings & Concepts

* Docker multi-stage builds
* Service dependency management
* Health checks in containers
* Reverse proxy setup (Nginx)
* Environment variable handling
* Microservice communication

---

## 🚧 Future Improvements

* Add **CI/CD pipeline (GitHub Actions)**
* Deploy on **AWS (EC2 / ECS / EKS)**
* Add **custom domain support**
* Rate limiting (Nginx / FastAPI middleware)
* Logging & monitoring (Prometheus + Grafana)
* Authentication for API usage

---

## 💼 Why This Project Matters

This project demonstrates real-world DevOps skills:

* Containerized microservices
* Production-ready architecture
* Infrastructure thinking (networking, proxy, health checks)
* Clean and scalable design

---

## 👨‍💻 Author

Chetan – Aspiring DevOps Engineer 🚀

---

## ⭐ If you like this project

Give it a star on GitHub ⭐

