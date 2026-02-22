FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# uv
RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

# instala deps en /app/.venv
RUN python3 -m uv sync --frozen

COPY . .

# para producción podrías quitar --reload (acá lo dejamos neutral)
CMD ["python3", "-m", "uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]