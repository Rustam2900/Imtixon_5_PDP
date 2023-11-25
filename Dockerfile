FROM python:3.11-slim
WORKDIR Imtixon
COPY . .
EXPOSE 3001

RUN pip install -r requirements.txt







CMD ["python", "main.py"]