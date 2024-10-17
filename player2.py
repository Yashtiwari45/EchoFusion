import streamlit as st
from pydub import AudioSegment
import concurrent.futures
from io import BytesIO
import librosa
import soundfile as sf
import numpy as np
from scipy.signal import butter, lfilter

# Function to slow down the audio using librosa for better quality
def slow_audio_librosa(y, sr, factor=0.75):
    try:
        y_slowed = librosa.effects.time_stretch(y, factor)
        return y_slowed
    except Exception as e:
        st.error(f"Error slowing audio: {e}")
        return y

# Function to apply reverb effect using librosa
def add_reverb(y, sr, reverb_amount=0.3, delay_ms=50, decay=0.5):
    try:
        delay_samples = int(sr * (delay_ms / 1000.0))
        y_reverb = np.zeros(len(y) + delay_samples)
        y_reverb[:len(y)] += y
        y_reverb[delay_samples:] += y * decay
        y_reverb = y_reverb / np.max(np.abs(y_reverb))
        return y_reverb[:len(y)]
    except Exception as e:
        st.error(f"Error adding reverb: {e}")
        return y

# Function to create a simple 8D audio effect by alternating left-right channels
def create_8d_effect(y, sr):
    try:
        y_stereo = np.array([y * np.sin(2 * np.pi * 0.2 * np.arange(len(y)) / sr),
                             y * np.cos(2 * np.pi * 0.2 * np.arange(len(y)) / sr)])
        return y_stereo.T
    except Exception as e:
        st.error(f"Error creating 8D effect: {e}")
        return y

# Function to apply a low-pass filter for lofi effect
def butter_lowpass_filter(data, cutoff, sr, order=5):
    try:
        nyquist = 0.5 * sr
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = lfilter(b, a, data)
        return y
    except Exception as e:
        st.error(f"Error applying lofi filter: {e}")
        return data

def add_lofi_effect(y, sr, cutoff=8000):
    try:
        y_lofi = butter_lowpass_filter(y, cutoff, sr)
        noise = np.random.normal(0, 0.001, len(y_lofi))
        return y_lofi + noise
    except Exception as e:
        st.error(f"Error adding lofi effect: {e}")
        return y

# Function to combine effects
def combine_effects(y, sr, effects):
    try:
        for effect in effects:
            if effect == "slowed":
                y = slow_audio_librosa(y, sr, factor=0.75)
            elif effect == "reverb":
                y = add_reverb(y, sr)
            elif effect == "8d":
                y = create_8d_effect(y, sr)
            elif effect == "lofi":
                y = add_lofi_effect(y, sr)
        return y
    except Exception as e:
        st.error(f"Error combining effects: {e}")
        return y

# Function to apply an effect on audio chunks in parallel
def apply_effect_in_parallel(y, sr, effect_function, chunk_duration_ms=30000):
    chunks = [y[i:i + chunk_duration_ms] for i in range(0, len(y), chunk_duration_ms)]
    processed_chunks = []
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            processed_chunks = list(executor.map(effect_function, chunks))
        return np.concatenate(processed_chunks)
    except Exception as e:
        st.error(f"Error processing audio in parallel: {e}")
        return y

# Function to convert numpy array to audio using soundfile
def save_audio_to_wav(y, sr):
    try:
        audio_buffer = BytesIO()
        sf.write(audio_buffer, y, sr, format='wav')
        audio_buffer.seek(0)
        return audio_buffer
    except Exception as e:
        st.error(f"Error saving audio to wav: {e}")
        return None

# Streamlit UI with enhanced CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1f4037, #99f2c8);
        font-family: 'Roboto', sans-serif;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(90deg, #fc466b, #3f5efb);
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        color: #fff;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #3f5efb, #fc466b);
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(255, 100, 150, 0.6);
    }
    .stFileUploader, .stSelectbox {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        padding: 10px;
    }
    .stSelectbox>div>div {
        color: white;
    }
    .stAudio {
        border: none;
        border-radius: 8px;
        overflow: hidden;
        background: rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        background: -webkit-linear-gradient(#fc466b, #3f5efb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Music Effect Converter with Multithreading</h1>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a music file...", type=["mp3", "wav"])

if uploaded_file is not None:
    audio = AudioSegment.from_file(uploaded_file)
    st.audio(uploaded_file)

    y, sr = librosa.load(BytesIO(audio.export(format="wav").read()), sr=None)

    effect = st.selectbox("Choose an effect", ("None", "Slowed", "Reverb", "8D", "Lofi", 
                                               "Lofi + 8D"))

    if st.button("Apply Effect"):
        if effect == "Slowed":
            audio_output = apply_effect_in_parallel(y, sr, lambda x: slow_audio_librosa(x, sr, factor=0.75))
        elif effect == "Reverb":
            audio_output = apply_effect_in_parallel(y, sr, lambda x: add_reverb(x, sr))
        elif effect == "8D":
            audio_output = create_8d_effect(y, sr)
        elif effect == "Lofi":
            audio_output = apply_effect_in_parallel(y, sr, lambda x: add_lofi_effect(x, sr))
        elif effect == "Lofi + 8D":
            audio_output = combine_effects(y, sr, ["lofi", "8d"])

        audio_buffer = save_audio_to_wav(audio_output, sr)
        audio_output_segment = AudioSegment.from_file(audio_buffer)

        audio_bytes = BytesIO()
        try:
            audio_output_segment.export(audio_bytes, format="mp3")
            audio_bytes.seek(0)
            st.audio(audio_bytes)
            st.download_button(label="Download Modified Audio", data=audio_bytes, file_name="modified_music.mp3", mime="audio/mp3")
        except Exception as e:
            st.error(f"Error exporting audio: {e}")
