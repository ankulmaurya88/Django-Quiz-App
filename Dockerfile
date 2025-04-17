# Use the official Python image as a base image
FROM python:3.9

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and libraries
RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && apt-get clean

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Run migrations and collect static files when the container is started (optional)
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose the port the app will run on (Optional)
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
