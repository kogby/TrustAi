# TAI DQ Website

**Frontend:** React, Tailwind  
**Backend:** Django, PostgreSQL (containerized with Docker)

---

## Project Overview

This project focuses on two major themes: **Data Quality (DQ)** and **Explainable AI (XAI)**. The goal is to automate workflows, reduce data processing costs, and improve reliability.

### Data Quality (DQ)
- Implements parametric and non-parametric imputation methods to enhance data usability.
- Evaluates imputation results using **Differential Entropy**, **Canonical Relative Entropy**, and correlation-based metrics.
- For more details about DQ: [EDASH Repository](https://github.com/forbes110/EDASH)

### Explainable AI (XAI)
- Combines **Active Learning** for user interaction and adaptability to customized data.
- Ensures process stability and parameter reduction with **Knowledge Distillation**.
- Enhances model interpretability using **SHAP** (SHapley Additive exPlanations) and **Counterfactual Explanations** to assist decision-making.

### Additional Resources
- [Presentation PPT](./專題簡報.pdf)  
- [Poster](./image/Poster.png)

---

## Demo

### Demo Video
[View Demo Video]()

### Website Preview
![Upload Page Screenshot](./image/upload_page.png)

---

## Setup Instructions

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Node.js & npm (for frontend)

### 1. Frontend Setup
The frontend runs on `http://localhost:5173/`.

```bash
cd frontend
npm install
npm run dev
```

### 2. Backend & Database Setup
The backend is containerized using Docker Compose.

1. Start Docker Desktop.
2. Build and start the backend and database:

```bash
cd backend
docker compose up --build
```

---

## Notes
- **CORS Policy** is handled using a Vite proxy configuration.
- If Docker is already set up, you can restart the backend without `--build`:

```bash
docker compose up
```

---

### Future Improvements
- Add unit testing for both frontend and backend.
- Integrate a CI/CD pipeline for automated deployments.
- Enhance database query optimization for large datasets.

---

## Contact
For questions or issues, feel free to raise a GitHub issue or contact the project maintainers.

---

Enjoy exploring the TAI DQ 🚀
