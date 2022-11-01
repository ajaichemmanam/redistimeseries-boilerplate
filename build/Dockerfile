FROM python:3.8-slim-buster

# Install dependencies
RUN pip3 install --upgrade redis==3.5.3 redistimeseries

# Copy /app directory
COPY app /app

# python3 /app/main.py
CMD ["python3", "/app/main.py"]
