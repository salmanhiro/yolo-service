FROM python:3.8-slim-buster

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y


COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

WORKDIR .

RUN wget https://pjreddie.com/media/files/yolov3.weights -P ./model

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]