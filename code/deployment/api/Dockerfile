FROM python:3.9-slim

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --upgrade pip

WORKDIR /api

COPY ./deployment/api/ . 

COPY ../../models/model.pkl /api/models/model.pkl

RUN pip install --no-cache-dir fastapi uvicorn pandas numpy==1.23.5 scikit-learn==1.2.2 joblib pydantic

EXPOSE 8001

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]
