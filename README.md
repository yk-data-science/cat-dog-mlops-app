# Cat-Dog MLops App

This repository contains a full-stack ML application that classifies images of cats and dogs (and optionally other animals). It includes:

- A trained machine learning model  
- A backend API built with Django or FastAPI  
- A React-based frontend  
- Dockerized setup and deployment workflow  

---

## Features

- Upload an image and get real-time classification (Cat / Dog / Other)  
- End-to-end pipeline: model training → inference API → frontend interaction  
- Modular and maintainable architecture, suitable for MLOps experiments  
- Ready for cloud deployment and CI/CD integration  

---

## Tech Stack

| Layer        | Tech                                       |
|--------------|--------------------------------------------|
| Frontend     | React, HTML/CSS                            |
| Backend      | Django (Django REST Framework)             |
| ML Model     | Simple CNN or pretrained model (e.g. MobileNet) |
| Image Format | JPEG, PNG supported                        |
| Container    | Docker, Docker Compose                     |
| Deployment   | Render.com / Heroku / AWS                  |

---

## Project Structure




- `cat-dog-mlops-app/`  
  - `backend/`  
    - `app/` — Main application logic  
    - `models/` — ML model integration  
    - `api/` — REST endpoints  
  - `frontend/`  
    - `public/`  
    - `src/`  
  - `ml_model/` — Training & inference code (`train_model.py`)  
  - `data/` — (Ignored) Dataset or image samples  
  - `notebooks/` — Training or EDA notebooks  
  - `scripts/` — Utility scripts (e.g., preprocessing)  
  - `docker/` — Docker setup files (`Dockerfile`)  
  - `requirements.txt` — Python dependencies  
  - `.gitignore`  
  - `README.md`  

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the model

```bash
python ml_model/train_model.py
```

### 3. Run backend API

```bash
cd backend
uvicorn app.main:app --reload
```

### 4. Start frontend

```bash
cd frontend
npm install
npm start
```

---

## Development & Deployment Flow

This project follows a basic full-stack MLops workflow:

1. **Build the React + Django app**  
   Create frontend and backend locally.

2. **Dockerize the app**  
   Write `Dockerfile` and `docker-compose.yml`.  
   Confirm it runs correctly in your local Docker environment.

3. **Push to GitHub**  
   Prepare the repository for deployment.

4. **Deploy to cloud**  
   Use Render.com, Heroku, or AWS to make the app public.

5. **Add CI/CD and MLOps features**  
   - Automate testing and deployment using GitHub Actions  
   - Optionally auto-update ML models upon data or code changes

---

## Docker

To run the entire app via Docker:

```bash
docker build -t cat-dog-app .
docker run -p 8000:8000 cat-dog-app
```

---

## License