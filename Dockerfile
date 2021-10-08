FROM python:3.8-slim-buster

RUN apt-get update -y
RUN apt install libgl1-mesa-glx wget libglib2.0-0 -y

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

WORKDIR .

RUN wget https://pjreddie.com/media/files/yolov3-tiny.weights -P /model

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]