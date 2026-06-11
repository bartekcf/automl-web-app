FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY streamlit_app.py .

CMD ["uv", "run", "streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]