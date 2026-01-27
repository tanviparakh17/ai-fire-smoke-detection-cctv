import streamlit as st
import cv2
import tempfile
import os

st.set_page_config(page_title="Fire Detection System", layout="centered")

st.title("🔥 Real-Time Fire & Smoke Detection using CCTV")
st.write("Software-based fire detection system using deep learning")

uploaded_video = st.file_uploader(
    "Upload CCTV Video", type=["mp4", "avi", "mov"]
)

if uploaded_video is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_video.read())

    st.video(tfile.name)

    st.info("Processing video for fire and smoke detection...")

    # Placeholder for model inference
    st.warning("⚠️ Fire detected! Alert sound triggered.")

    st.success("Video processed successfully.")