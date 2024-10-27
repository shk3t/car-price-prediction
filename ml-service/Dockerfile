FROM python:3.12-alpine
WORKDIR /ml-service
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD pytest -q --tb=no $TARGET