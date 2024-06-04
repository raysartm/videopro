import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import streamlit as st
import cv2
from tempfile import NamedTemporaryFile
from moviepy.editor import VideoFileClip

def process_video(input_video_path):
    # Read the input video
    video = cv2.VideoCapture(input_video_path)
    
    # Process the video (in this example, just reverse it)
    frames = []
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)
    
    # Reverse the frames
    reversed_frames = frames[::-1]
    
    # Write the processed frames to a new video file
    output_video_path = NamedTemporaryFile(suffix='.mp4').name
    height, width, _ = reversed_frames[0].shape
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
    for frame in reversed_frames:
        out.write(frame)
    out.release()
    
    return output_video_path

# Streamlit app
st.title("Video Processing App")

# Upload video file
uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])

# Process the video when button is clicked
if uploaded_file is not None:
    if st.button("Process Video"):
        with st.spinner("Processing..."):
            output_video_path = process_video(uploaded_file)
        st.success("Video processed successfully!")
        
        # Display the processed video
        st.video(output_video_path)

