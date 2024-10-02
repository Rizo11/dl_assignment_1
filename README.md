# PDLML course assignment 1

by Mukhammadrizo Maribjonov BS2-RO-01

### structure
```
assig1/
├── code
│   ├── datasets
│   ├── deployment
│   │   ├── api
│   │   │   ├── api.py              # FastAPI code for the model API
│   │   │   ├── Dockerfile          # Dockerfile for FastAPI
│   │   └── app
│   │       ├── app.py              # Streamlit app code
│   │       ├── Dockerfile          # Dockerfile for Streamlit
│   ├── models
│   │   └── model.pkl               # Saved machine learning model
├── data
├── models
│   └── (optional, could be empty if models are too large for GitHub)
└── docker-compose.yml              # Docker Compose file to orchestrate the app and API

README.md                           # Description of project, steps to run it
```

### code explanation

#### FastAPI:
* Data Input: We're using a `pydantic` `BaseModel` class to receive input features (`assignment_in_class`, `assignment_1`, `assignment_midterm`).
* Data Preprocessing:
* Missing values (e.g., '-', empty spaces) are replaced with `NaN`.
* Numeric conversion is applied with error handling.
* Imputation and scaling are performed using a `SimpleImputer` and `StandardScaler`.
* Prediction: After preprocessing, the model makes a prediction on the transformed input data.

#### Streamline

#### Docker files
* `FastAPI` Dockerfile:
  * It copies the model into the container.
  * It installs necessary dependencies (`FastAPI`, Uvicorn, pandas, numpy, scikit-learn, etc.).
  * It runs `FastAPI` with `uvicorn` and exposes port `8000`.
* `Streamlit` Dockerfile:
  * It installs necessary dependencies (`streamlit`, requests).
  * It runs `Streamlit` and exposes port `8501`.
* docker-compose.yml:
  * The `FastAPI` service (api) and `Streamlit` service (app) are both defined.
  * The `Streamlit` service depends on the `FastAPI` service, ensuring the API runs first.
  * Volumes are used to link the models from the host system to the `FastAPI` container.