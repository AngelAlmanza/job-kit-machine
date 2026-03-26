FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar uv para manejo de dependencias
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copiar archivos de dependencias
COPY pyproject.toml ./

# Instalar dependencias
RUN uv pip install --system -r pyproject.toml

# Copiar código fuente
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
