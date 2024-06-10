import cv2
import os
from tempfile import NamedTemporaryFile

def slow_motion(input_video_path):
    try:
        cap = cv2.VideoCapture(input_video_path)
        if not cap.isOpened():
            raise ValueError("Unable to open video file:", input_video_path)

        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = cap.get(cv2.CAP_PROP_FPS)
        new_fps = 10  # Adjust the frame rate as needed

        with NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
            temp_filename = temp_file.name

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            output = cv2.VideoWriter(temp_filename, fourcc, new_fps, (width, height))

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                output.write(frame)

            output.release()
            cap.release()

        return temp_filename

    except Exception as e:
        print(f"Error in slow_motion: {e}")
        return None
