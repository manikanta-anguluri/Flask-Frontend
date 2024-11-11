# Base image
FROM python:3.10

# Install system dependencies
RUN apt-get update

# Set the working directory in the container
WORKDIR /code

# Copy the rest of the application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Apply migrations and run Django development server
CMD python app.py --debug run