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
git clone https://github.com/panche20/url-shortener-app.git
cd url-shortener-app
```

### 2️⃣ Start services

```bash
docker-compose up --build
```

### 3️⃣ Access application

* App: http://localhost/80
* Health: http://localhost/health

---

## 🔗 API Endpoints

### ➤ Create Short URL

```bash
# Health check
curl http://localhost/health
# {"status":"healthy","redis":"connected"}
```

Shorten a URL:

```
curl -X POST http://localhost/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'
# {"short_code":"abc123","short_url":"/r/abc123"}
```

Use your actual short code from above:

```
curl -L http://localhost/r/abc123
# Redirects to google.com
```

---

### ➤ Check click stats

```
curl http://localhost/stats/abc123
# {"short_code":"abc123","url":"https://www.google.com","clicks":"1"}
```

---

### ➤ Shorten a few more

```
curl -X POST http://localhost/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com"}'
```

Hit it a few times and watch clicks increment:

```
curl http://localhost/stats/abc123
```

---

### ➤ Prove Persistence Survives Restarts

```
Shorten something, note the code
curl -X POST http://localhost/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com"}'
```

Destroy and recreate everything (keep volumes)
```
docker compose down
docker compose up -d
```

Your data is still there
```
curl http://localhost/stats/<your_code>
```

Inspect What You Built
```
Layer history — see your multi-stage work
docker history url-shortener-app --no-trunc
```

Verify no secrets in the image
```
docker inspect url-shortener-app-1 \
  --format '{{range .Config.Env}}{{.}}{{"\n"}}{{end}}'
```

Check non-root user is running the process
```
docker compose exec app whoami
# appuser ← not root, good
```

Check what's actually in /app — should be clean
```
docker compose exec app find /app -type f
```

## For Kubernetes project - Create namespace, secrets, deployment & services

```
kubectl create ns url-shortener
kubectl config set-context --current --namespace=url-shortener
kubectl config view --minify | grep -i namespace
```

```
export SECRET_KEY="my-super-secret-app-key-$(openssl rand -hex 16)"
kubectl create secret generic app-secrets \
  --from-literal=redis_password=strongpassword123 \
  --from-literal=secret_key="$SECRET_KEY" \
  -n url-shortener
```

Then, apply url-shortener-deployment.yaml, redis-deployment.yaml, app-nodeport.yaml, app-service.yaml.
To test the app, follow below steps:

```
minikube ip
curl http://$(minikube ip):30080/health
```

To test the URL shortener functionality,
```
# See everything running
kubectl get all -n url-shortener
```
Port-forward to test locally
```
kubectl port-forward svc/url-shortener 8080:80 -n url-shortener &
```
Test the full stack
```
curl http://localhost:8080/health
```

```
curl -X POST http://localhost:8080/shorten \
  -H "Content-Type: application/json" \
  -d '{"url":"https://github.com"}'
```
Grab the code from response and test redirect
```
CODE=<your-code>
curl -L http://localhost:8080/r/$CODE

curl http://localhost:8080/stats/$CODE
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

Chetan – DevOps Engineer 🚀

---

## ⭐ If you like this project

Give it a star on GitHub ⭐

