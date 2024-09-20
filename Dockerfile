# Use a imagem oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos de requirements e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante da aplicação
COPY . .

# Exponha a porta que o serviço vai usar
EXPOSE 8000

# Comando para rodar a aplicação (ajuste conforme necessário)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "setup.wsgi:application"]
