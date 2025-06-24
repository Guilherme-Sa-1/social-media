# Dockerfile

FROM python:3.10-buster

WORKDIR /app

# Instala Poetry
RUN pip install poetry --no-cache-dir

# Copia os arquivos do projeto
COPY pyproject.toml poetry.lock ./

# Instala as dependências sem instalar o próprio projeto
RUN poetry install --no-root

# Copia o restante do projeto
COPY . .

# Comando para iniciar (ajuste conforme necessário)
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
