import streamlit as st
import cv2
from PIL import Image
import tensorflow as tf
import numpy as np
from lib import detect_expression
import tempfile


def main():
    st.title("Facial Expression Recognition")

    option = st.sidebar.selectbox(
        "Choose an option to detect and classify facial expressions.",
        ("Built-in Webcam", "External Camera", "Image or Video"),
    )
    frame_skip_rate = 5  # Best optimize frame

    if option == "Built-in Webcam":
        # webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
        vid = cv2.VideoCapture(0)
        if not vid.isOpened():
            st.error(
                "Failed to recognize built-in camera. Please choose other options."
            )
        else:
            st.title("Using Webcam with Streamlit")
            frame_window = st.image([])

            frame_count = 0  # Initialize frame count
            while True:
                got_frame, frame = vid.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if got_frame:
                    if frame_count % frame_skip_rate == 0:  # Process this frame
                        frame_window.image(detect_expression(frame))
                frame_count += 1

    elif option == "External Camera":
        camera_address = st.text_input(
            "Camera Address (e.g: http://192.168.137.101:4747/video)"
        )
        if camera_address:
            vid = cv2.VideoCapture(camera_address)
            st.title("Using Mobile Camera with Streamlit")
            frame_window = st.image([])

            frame_count = 0  # Initialize frame count
            while True:
                got_frame, frame = vid.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if got_frame:
                    if frame_count % frame_skip_rate == 0:  # Process this frame
                        frame_window.image(detect_expression(frame))
                frame_count += 1  # Increment frame count

    elif option == "Image or Video":
        uploaded_file = st.file_uploader(
            "Choose an image or video file", type=["jpg", "jpeg", "png", "mp4"]
        )
        if uploaded_file is not None:
            file_extension = uploaded_file.name.split(".")[-1]
            if file_extension in ["jpg", "jpeg", "png"]:
                image = Image.open(uploaded_file)
                image = np.array(image.convert("RGB"))
                image = detect_expression(image)
                st.image(image, channels="RGB", caption="Processed Image")
            elif file_extension == "mp4":
                st.write(frame_skip_rate)
                tfile = tempfile.NamedTemporaryFile(delete=False)
                tfile.write(uploaded_file.read())

                video_file = tfile.name

                # New replay flag and button
                replay_video = False
                replay_button = st.button("Replay Video")

                while True:
                    vid = cv2.VideoCapture(video_file)
                    frame_window = st.image([])

                    frame_count = 0  # Initialize frame count
                    while True:
                        got_frame, frame = vid.read()
                        if not got_frame:
                            st.write("End of video")
                            replay_video = False
                            if (
                                replay_button
                            ):  # If replay button is clicked, set the replay flag
                                replay_video = True
                            break  # Exit the loop if video has ended
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        if frame_count % frame_skip_rate == 0:  # Process this frame
                            processed_frame = detect_expression(frame)
                            frame_window.image(processed_frame)
                        frame_count += 1  # Increment frame count

                    if (
                        not replay_video
                    ):  # If replay flag is not set, break the outer loop
                        break


if __name__ == "__main__":
    gpus = tf.config.list_physical_devices("GPU")
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.list_logical_devices("GPU")
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)
    main()
