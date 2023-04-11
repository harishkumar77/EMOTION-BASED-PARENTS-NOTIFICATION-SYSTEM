import pyaudio
import wave
import sys
import os
import librosa
import numpy as np
import tensorflow as tf
from pushbullet import Pushbullet
from sklearn.preprocessing import OneHotEncoder

# Set the parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 60

# Create an instance of PyAudio
audio = pyaudio.PyAudio()

# Open a new stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording started... Press 'q' to stop recording.")
frames = []

# Record audio in chunks until user presses 'q'
while True:
    data = stream.read(CHUNK)
    frames.append(data)
    if len(data) == 0:
        break
    if 'q' in str(input()):
        break

print("Recording stopped.")

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio as a WAV file
waveFile = wave.open("E:/downloads/my_voice.wav", 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

file_path = "E:/downloads/my_voice.wav"

if os.path.exists(file_path):
    model = tf.keras.models.load_model("E:/downloads/lstm_model_SLP.h5")
    filename = "E:/downloads/my_voice.wav"
    audio, sample_rate = librosa.load(filename, sr=22050, mono=True, duration=5)

    # Extract features
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    features = np.mean(mfccs.T, axis=0)

    # Reshape the features to match the expected input shape of the model
    features = features.reshape(1, -1)

    # Load the encoder and fit it with the labels
    enc = OneHotEncoder()
    enc.fit([["fear"], ["angry"], ["disgust"], ["neutral"], ["sad"], ["pleasant"], ["happy"]])

    # Predict the label for the audio file
    predicted_class = model.predict(features)
    predicted_class_name = enc.inverse_transform(predicted_class)

    print("Predicted class:", predicted_class_name[0])

    if predicted_class_name[0] == "sad":
        API_KEY = "o.z0RIUOR99iHWkJ2GMg4mciGYbJzSQAuN"
        pb = Pushbullet(API_KEY)
        text = "your children seems to be sad in her conversation please take care of your children"
        push = pb.push_note("Sadness Detected", text)
