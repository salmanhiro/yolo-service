FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN wget https://pjreddie.com/media/files/yolov3.weights -P ./model
COPY . .

WORKDIR .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]