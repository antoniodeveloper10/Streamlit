# Usa a imagem base
FROM python:3.11-slim


# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências de sistema necessárias para o MySQL
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo requirements.txt primeiro
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . /app

# Expõe a porta do Streamlit
EXPOSE 8501

# Comando padrão para iniciar o Streamlit
CMD ["streamlit", "run", "index.py"]
