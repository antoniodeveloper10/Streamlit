import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import cv2
import numpy as np

st.title("Leitor de QR Code em tempo real - Streamlit Cloud / Celular")

class QRCodeProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame):
        img = frame.to_ndarray(format="bgr24")
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            st.session_state['qr_data'] = data
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="qr-code", video_processor_factory=QRCodeProcessor)

if 'qr_data' in st.session_state:
    st.success(f"QR Code detectado: {st.session_state['qr_data']}")
