FROM python:3.12-slim
WORKDIR /ml-service
RUN apt update
RUN apt install -y libpq-dev gcc
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# CMD python manage.py migrate ; python manage.py runserver --noreload
CMD python manage.py runserver --noreload