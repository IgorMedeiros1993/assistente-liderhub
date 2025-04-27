# Utilizar uma imagem Python oficial
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY . .

# Instalar dependências
RUN pip install -r requirements.txt

# Executar aplicação
CMD ["python", "app.py"]