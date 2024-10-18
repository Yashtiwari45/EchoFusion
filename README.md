# EchoFusion

Below, you will find a step-by-step overview of the application, focusing on the specific features, functionalities, and technical details:

### EchoFusion App

#### Description
The EchoFusionr app permits the uploading of audio files and adding many audio effects for listening purposes. The converter supports all common formats, such as MP3 and WAV, and offers modern design and solid functionality.

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

--


## Output(current progress)

### 1st Page [Login]
![Screenshot 2024-10-18 112224](https://github.com/user-attachments/assets/7ec21a62-2051-493a-ab4a-e457b031d0ce)

### 2nd page [Home]
![Screenshot 2024-10-17 125414](https://github.com/user-attachments/assets/8ac80ec3-bee8-4fc9-8dd2-7abd612c206d)





### Future Plans 
1. **Rich Audio Effects Library**
   More Effects: In addition to the already wide variety of effects like distortion, flanger, echo, and pitch shifting, more effects are added so that the users have even more choices for creativity.
   Custom Effect Design: Allow a user to design and save his custom audio effects by making combinations of different parameters of these effects, thus promoting creativity and personalization.

2. **Real-time Audio Processing**
- **Live Preview**: Integrating live preview functionality to the users, so they can hear the effects immediately after adjusting the parameters, thus creating immense interactivity with immediate feedback.
- **Interactive Mixing Console**: A virtual mixing console with multiple tracks and effects to play with.

3. **AI Driven Features
- Intelligent Audio Analysis: it uses the power of machine learning algorithms to analyze audio files so you can recommend suitable effects on the basis of the type of music or the mood of a track. In this way, each user gets relevant recommendations.
- Music Genre Classification: auto-classify feature implementable, wherein it identifies the genres of the uploaded tracks and applies the presets of the genre with which it identifies.

- 4. Mobile Application Development

- **Cross-Mobile Compatibility**: Develop for iOS and Android to make the Music Effect Converter available for in-field use, thus allowing for creation and editing of audio from any location.
   - **Cloud-Based Solution**: Integrate cloud storage solutions in such a way that a user's projects and audio files are saved securely and retrieved at ease from any location.

5. **Parsing of YouTube Link
- **YouTube Direct Integration**: Accept a YouTube link, parse it so audio can be taken from videos. This would prevent a user from having to download audio files and then add effects. It also provides options for the optimum quality and preferably format size before processing.


--

