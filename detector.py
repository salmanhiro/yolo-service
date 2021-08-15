import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_objects(input_image):
    col1, col2 = st.columns(2)

    col1.subheader("Sample Image")
    st.text("")
    plt.figure(figsize = (15,15))
    plt.imshow(input_image)
    col1.pyplot(use_column_width=True)

    # Read weights and config
    net = cv2.dnn.readNetFromDarknet("./model/yolov3.cfg", "./model/yolov3.weights")
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    # Load classes into different colors
    classes = []
    with open("./model/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

    colors = np.random.uniform(0,255,(len(classes), 3))

    new_img = np.array(input_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    height,weight,ch = img.shape
    # detect image from cv2 blob
    blob = cv2.dnn.blobFromImage(img, 1./255, (416,416), (104, 117, 123), swapRB = False, crop = False)   

    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    bboxes =[]

    # SHOWING INFORMATION CONTAINED IN 'outs' VARIABLE ON THE SCREEN
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)  
            confidence = scores[class_id] 
            if confidence > 0.5:   
                # OBJECT DETECTED
                #Get the coordinates of object: center,width,height  
                center_x = int(detection[0] * weight)
                center_y = int(detection[1] * height)
                w = int(detection[2] * weight)  #width is the original width of image
                h = int(detection[3] * height) #height is the original height of the image

                # RECTANGLE COORDINATES
                x = int(center_x - w /2)   #Top-Left x
                y = int(center_y - h/2)   #Top-left y

                #To organize the objects in array so that we can extract them later
                bboxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    score_threshold = st.sidebar.slider("Confidence Threshold", 0.00,1.00,0.5,0.01)
    nms_threshold = st.sidebar.slider("NMS Threshold", 0.00, 1.00, 0.5, 0.01)

    indexes = cv2.dnn.NMSBoxes(bboxes, confidences, score_threshold,nms_threshold)      
    print(bboxes, confidences)

    font = cv2.FONT_HERSHEY_SIMPLEX
    items = []
    for i in range(len(bboxes)):
        if i in indexes:
            x,y,w,h = bboxes[i]
            #To get the name of object
            label = str.upper((classes[class_ids[i]]))   
            color = colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)     
            cv2.putText(img, label, (x-5,y-5), font, 
                   1, color, 1, cv2.LINE_AA)
            items.append(label)

    st.text("")
    col2.subheader("Object-Detected Image")
    st.text("")
    plt.figure(figsize = (15,15))
    plt.imshow(img)
    col2.pyplot(use_column_width=True)


    st.success("Found {} Object(s) - {}".format(len(indexes),",".join(items)))
