# # Use the official Python image as a base image
# FROM python:3.9

# # Set environment variables to prevent Python from writing .pyc files and buffering output
# ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /app

# # Install system dependencies and libraries
# RUN apt-get update \
#     && apt-get install -y libpq-dev gcc \
#     && apt-get clean

# # Copy the requirements.txt file into the container
# COPY requirements.txt /app/

# # Install Python dependencies inside the container
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the project files into the container
# COPY . /app/

# # Run migrations and collect static files when the container is started (optional)
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# # Expose the port the app will run on (Optional)
# EXPOSE 8000

# # Run the Django application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# Use official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run Django app with gunicorn
CMD ["gunicorn", "Quiz.wsgi:application", "--bind", "0.0.0.0:8000"]
