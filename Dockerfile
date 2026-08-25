# ---- Builder ----
FROM python:3.11-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable

# ---- Runtime ----
FROM python:3.11-slim

COPY --from=builder /app/.venv /app/.venv
COPY app/ /app/app/

ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]