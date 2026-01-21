# Before Docker Mulit-Staging.
# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 5000

# CMD ["python", "app.py"]


# After Multi Staging.
# ---------- STAGE 1: Install dependencies ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

# Install Python libraries into a temporary folder
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- STAGE 2: Run application ----------
FROM python:3.11-slim

WORKDIR /app

# Copy only installed libraries from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

 









