# Music-Effect-converter

Below, you will find a step-by-step overview of the application, focusing on the specific features, functionalities, and technical details:

### Music Effect Converter App

#### Description
The Music Effect Converter app permits the uploading of audio files and adding many audio effects for listening purposes. The converter supports all common formats, such as MP3 and WAV, and offers modern design and solid functionality.

#### Main Features
1. **Audio Upload** :
- Audio files can be uploaded in either MP3 or WAV format for processing purposes.

2. **Audio Effects**:
   **Slowed**: It slows down the audio to listen at a slower pace, as if giving your ears a calm experience.
   **Reverb**: Adds a reverb effect to the audio so that it gives space and depth to it.
- **8D Audio**: Creates the perception of a 3D audio experience by switching audio between left and right channels.
   - **Lofi**: Uses a low-pass filter for a nostalgic, warm audio that sounds like it is coming from a vinyl record.

3. **Cumulative Effects**:
   - Users can apply accumulative effects; for example: "Lofi + 8D" or "Slowed + Reverb," which gives a custom audio experience.

4. **Real-time Audio Processing**
It utilizes `librosa` and `pydub` to carry out efficient manipulations on audio, as well as `concurrent.futures` in order to take advantage of multithreading, which makes it perform faster when processing chunks of audio.

5. **Downloadable Output**:
   The output generated after processing can be downloaded as an MP3 format of the modified audio file by the users.

6. **Dynamic User Interface**:
   The application comes with an animated and an aesthetically pleasing interface built with Streamlit, which makes the users more interactive and interesting.

#### Technical Implementation
- Libraries Used:
- `streamlit`: To generate the interactive web interface.
  - `pydub`: Audio files manipulation.
  - `librosa`: Time-stretching audio and adding effects.
  - `numpy` and `scipy`: Numerical computations and effect implementations, such as filtering and reverb.

- **Audio Processing Functions**
  - Slow Audio: Making use of `librosa.effects.time_stretch()` for a high-quality slowdown of audio.
- **Reverb**: There is a custom reverb effect created by using a delay and decay approach.
  - **8D Effect**: Creates the sound of a stereo by changing audio channels.
  - **Lofi Effect**: Applies a low-pass filter combined with noise to create a vintage sound.
- **Concurrency**:
  - Audio processing will run in parallel using multithreading, which improves performance with larger files.

