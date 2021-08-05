FROM python:3
WORKDIR /home/nada/flusktodo/app.py
COPY . .
CMD ["python", "./app.py"]
