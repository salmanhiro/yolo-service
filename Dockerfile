FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

    
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN wget https://pjreddie.com/media/files/yolov3.weights -P ./model
COPY . .



WORKDIR .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]