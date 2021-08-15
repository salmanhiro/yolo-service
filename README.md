# yolo-service
Yolo in streamlit service 


# How to build

## Using docker

`docker build -t yolo-service .`
`docker run -dp 8501:8501 yolo-service`

## Directly

Download the weight file from https://pjreddie.com/media/files/yolov3.weights and put under the model folder. 
run `streamlit run app.py`

References: 
```
Redmon, Joseph, and Ali Farhadi. Yolov3: An incremental improvement. arXiv preprint arXiv:1804.02767 (2018). https://pjreddie.com/darknet/yolo/
Gupta, Srishti. Object Detection App using YOLOv3, OpenCV and Streamlit. https://srishti.hashnode.dev/object-detection-app-using-yolov3-opencv-and-streamlit-1
```
