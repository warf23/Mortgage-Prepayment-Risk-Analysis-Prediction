# Use an official Python runtime as a parent image
FROM python:3.10.9

# Set the working directory in the container
WORKDIR /application

# Copy the current directory contents into the container at /app
COPY . /application

# Install any needed packages specified in requirements.txt

RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt


# Run application.py when the container launches
CMD ["python3", "application.py" , "--port", "8080"]
