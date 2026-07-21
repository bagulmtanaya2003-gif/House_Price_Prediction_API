# 🏠 House Price Prediction API

## 📌 Project Overview

House Price Prediction API is an end-to-end Machine Learning deployment project that predicts house prices based on user-provided input features.

The project includes data preprocessing, feature encoding, Machine Learning model training, and deployment of the trained model using FastAPI. Docker is used to containerize the application and create a consistent deployment environment.

## 🚀 Features

- Data cleaning and preprocessing
- Feature encoding for categorical variables
- Machine Learning model training
- Real-time house price prediction API
- FastAPI REST API development
- Interactive Swagger API documentation
- Docker containerization

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning & Data Processing
- Pandas
- NumPy
- Scikit-learn
- Joblib

### API Development
- FastAPI
- Uvicorn

### Deployment
- Docker

## 📂 Project Structure

```
HOUSE_PRICE_PREDICTION

│
├── app.py                    # FastAPI application
├── house_price_model.pkl     # Trained Machine Learning model
├── encoder.pkl               # Saved feature encoder
├── clean_housing.csv         # Cleaned dataset
├── requirements.txt          # Required Python libraries
├── Dockerfile                # Docker configuration file
├── README.md                 # Project documentation
│
└── screenshots
    ├── swagger_ui.png
    ├── prediction_result.png
    └── docker_container.png
```

# ⚙️ How to Run the Project Locally

Follow these steps to run the House Price Prediction API on your local system.

## 1. Clone the Repository

Download the project from GitHub:

```bash
git clone <your-github-repository-link>
```

Go inside the project folder:

```bash
cd HOUSE_PRICE_PREDICTION
```
## 2. Install Required Dependencies

Install all required Python libraries:

```bash
pip install -r requirements.txt
```
The requirements file contains all dependencies required to run the FastAPI application.

## 3. Start FastAPI Application

Run the API server using:

```bash
uvicorn app:app --reload
```
Explanation:

- `app` → Python file name (`app.py`)
- `app` → FastAPI application object created inside the file
- `--reload` → Automatically restarts server when code changes

After successful execution, the API will start running locally.

## 4. Open Swagger API Documentation

Open your browser:

```
http://127.0.0.1:8000/docs
```
FastAPI Swagger UI allows users to:

- View available API endpoints
- Enter house details
- Test prediction requests
- Get predicted house prices

# 🐳 Docker Deployment

Docker is used to package the application with all dependencies and run it inside a container.

## 1. Build Docker Image

Create a Docker image:

```bash
docker build -t house-price-api .
```

## 2. Run Docker Container

Start the application container:

```bash
docker run -d --name house-price-container -p 8000:8000 house-price-api
```

Explanation:

- `-d` → Runs container in background
- `--name` → Assigns container name
- `-p 8000:8000` → Maps local port with container port

## 3. Check Running Container

Verify Docker container:

```bash
docker ps
```

## 4. Access API

Open:

```
http://localhost:8000/docs
```

Swagger UI will be available for testing predictions.

# 📸 API Screenshots

## Swagger UI

FastAPI interactive documentation:

```
screenshots/swagger_ui.png
```

## Prediction Output

Sample prediction result:

```
screenshots/prediction_result.png
```

## Docker Container

Running Docker container:

```
screenshots/docker_container.png
```

# 📊 Dataset

Dataset used for training:

**Kaggle House Price Dataset**

The dataset was cleaned and preprocessed before training the Machine Learning model.

Data preprocessing steps include:

- Handling missing values
- Feature transformation
- Encoding categorical features
- Preparing data for model training

# 🤖 Machine Learning Model

The trained Machine Learning model is saved using Joblib.

Model file:

```
house_price_model.pkl
```

Feature encoder:

```
encoder.pkl
```

These saved files are loaded by FastAPI during prediction requests.

# 🔄 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Saving using Joblib
7. FastAPI API Development
8. Docker Deployment

# 🔮 Future Improvements

- Deploy API on AWS / Azure cloud
- Add frontend interface using Streamlit or React
- Implement model monitoring
- Improve model performance
- Add database integration

# 👩‍💻 Author

**Tanaya Bagul**

Machine Learning | Data Science | FastAPI | Docker