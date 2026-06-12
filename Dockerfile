ARG PYTHON_VERSION=3.11-slim

FROM python:${PYTHON_VERSION} AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:${PYTHON_VERSION}

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r brihaspati && useradd -r -g brihaspati brihaspati

COPY --from=builder /root/.local /home/brihaspati/.local
ENV PATH=/home/brihaspati/.local/bin:$PATH

COPY --chown=brihaspati:brihaspati backend/ backend/
COPY --chown=brihaspati:brihaspati configs/ configs/
COPY --chown=brihaspati:brihaspati vector_db/ vector_db/

USER brihaspati

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
