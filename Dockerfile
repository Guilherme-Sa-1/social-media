# Dockerfile

FROM python:3.10-buster

# Instala dependências básicas
WORKDIR /app

# Instala o Poetry
RUN pip install poetry --no-cache-dir

# Copia arquivos necessários para instalar dependências
COPY pyproject.toml poetry.lock ./

# Instala as dependências (sem instalar o projeto como pacote)
RUN poetry install --no-root

# Copia o restante do código para a imagem
COPY . .

# Expõe a porta usada pelo Uvicorn
EXPOSE 8000

# Comando para iniciar a aplicação via Taskipy
CMD ["poetry", "run", "task", "prod"]
