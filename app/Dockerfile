# FROM python:3.9-slim

# WORKDIR /app/
# COPY . .

# RUN python3 -m venv venv
# RUN source /venv/bin/pip install -r requirements.txt

# CMD ["/venv/bin/python", "app.py"]
FROM python:3.9-slim-bullseye

RUN python3 -m venv venv

# Install dependencies:
COPY requirements.txt .
RUN . /venv/bin/activate && pip install -r requirements.txt

# Run the application:
COPY . .
CMD . /venv/bin/activate && exec python3 app.py