# Base image
FROM python:3.8.10-alpine

# Set directory
WORKDIR /app

# Enviroments
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

# Run commands to upgrade and add packages 
RUN apk update && \
    apk add --virtual build-essential gcc python3-dev musl-dev && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    apk --purge del .build-deps && \
    apk add gettext

# Copy libs
COPY requirements.txt . 

# Upgrade pip and install requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project 
COPY . .

# Expose port 8000
EXPOSE 8000

# Run server
CMD python manage.py runserver 0.0.0.0:8000
