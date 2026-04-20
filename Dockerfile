FROM python:3.14
WORKDIR /app
COPY . .
Run pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]