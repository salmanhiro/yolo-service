import streamlit as st
from PIL import Image
from detector import detect_objects

def object_main():
    st.set_option('deprecation.showPyplotGlobalUse', False)


    st.title("YOLOv3 Object Detection")
    introduction = open("intro.txt", "r")
    st.write(str(introduction.read()))

    st.write('Note: I do not store your image since I am not planning to invest on storage. I am broke')
    st.write("\n")

    choice = st.radio("", ("Show Sample", "Browse your Image"))

    if choice == "Browse your Image":
        st.set_option('deprecation.showfileUploaderEncoding', False)
        image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

        if image_file is not None:
            our_image = Image.open(image_file)  
            
            detect_objects(our_image)

    else:
        our_image = Image.open("images/sampleimg.jpg")
        detect_objects(our_image)

    
    st.write("References: ")
    st.markdown("`Redmon, Joseph, and Ali Farhadi. Yolov3: An incremental improvement. arXiv preprint arXiv:1804.02767 (2018). https://pjreddie.com/darknet/yolo/`")
    st.markdown("`Gupta, Srishti. Object Detection App using YOLOv3, OpenCV and Streamlit. https://srishti.hashnode.dev/object-detection-app-using-yolov3-opencv-and-streamlit-1`")

    st.write("Repository")
    st.markdown("`https://github.com/salmanhiro/yolo-service`")
    

if __name__ == '__main__':
    object_main()
