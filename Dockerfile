FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install Poetry and dependencies
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./ 

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Set environment variables
ENV HOST=0.0.0.0

# Development-specific command for auto-reload
CMD ["poetry", "run", "uvicorn", "src:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

