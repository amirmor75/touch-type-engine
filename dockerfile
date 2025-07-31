# backend/Dockerfile
FROM python:3.11-slim-bullseye

# Install system dependencies and clean up to reduce vulnerabilities
RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential wait-for-it \
	&& apt-get upgrade -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get remove --purge -y build-essential \
	&& apt-get autoremove -y

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the app port
EXPOSE 8000

# Run the app
CMD ["wait-for-it", "db:5432", "--", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

	