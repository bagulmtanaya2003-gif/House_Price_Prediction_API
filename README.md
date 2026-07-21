# 🏠 House Price Prediction API

A Machine Learning powered REST API built using FastAPI and Docker to predict house prices based on property details.

---

## 📌 Project Overview

This project predicts house prices using a trained Machine Learning model. Users can send house details through a FastAPI endpoint and receive the predicted house price instantly.

The API is containerized using Docker, making deployment and execution simple across different environments.

---

## 🚀 Features

- Predict house prices using Machine Learning
- FastAPI REST API
- Interactive Swagger Documentation
- Docker Support
- Input Validation
- JSON Response
- Clean Project Structure

---

## 🛠 Tech Stack

- Python
- FastAPI
- Pandas
- Scikit-learn
- Joblib
- Docker
- Swagger UI

---

## 📂 Project Structure

House_Price_Prediction/

├── app.py

├── house_price_model.pkl

├── encoder.pkl

├── requirements.txt

├── Dockerfile

├── README.md

└── screenshots/

    ├── 01_api_docs_overview.png

    ├── 02_predict_input_form.png

    ├── 03_predict_response.png

    ├── 04_home_endpoint.png

    ├── 05_docker_running.png

    ├── 06_correlation_heatmap.png

    ├── 07_price_distribution.png

    └── 08_squarefeet_vs_price.png

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/bagulmtanaya2003-gif/House_Price_Prediction.git
```

Move into the project

```bash
cd House_Price_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app:app --reload
```

Open Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker

Build Docker Image

```bash
docker build -t house-price-api .
```

Run Docker Container

```bash
docker run -d --name house-price-container -p 8000:8000 house-price-api
```

Open

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Home

GET /

Returns welcome message.

---

### Prediction

POST /predict

Input Parameters

| Parameter | Type |
|------------|------|
| SquareFeet | Integer |
| Bedrooms | Integer |
| Bathrooms | Integer |
| Neighborhood | Rural / Suburb / Urban |
| YearBuilt | Integer |

Response

```json
{
    "Predicted Price": 425678.91
}
```

---

# 📷 Project Screenshots

## API Documentation

- [01 API Docs Overview](screenshots/01_api_docs_overview.png.png)

---

## Prediction Input

- [02 Predict Input Form](screenshots/02_predict_input_form.png.png)
---

## Prediction Result

- [03 Predict Response](screenshots/03_predict_response.png.png)

---

## Home Endpoint

- [04 Home Endpoint](screenshots/04_home_endpoint.png.png)
---

## Docker Container Running

- [05 Docker Running](screenshots/05_docker_running.png.png)


---

## Correlation Heatmap

- [Correlation Heatmap](screenshots/Correlation%20Heatmap.png)

---

## Price Distribution

- [Price Distribution](screenshots/Price%20Distribution.png)

---

## Square Feet vs Price

- [SquareFeet_vs_price](screenshots/squarefeet_vs_price.png)
---

## Future Improvements

- Deploy on Render
- Database Integration
- Authentication
- Model Retraining
- CI/CD Pipeline

---

## Author

Tanaya Bagul

GitHub

https://github.com/bagulmtanaya2003-gif

LinkedIn

www.linkedin.com/in/tanaya-bagul-b21354285

Machine Learning | Data Science | FastAPI | Docker
