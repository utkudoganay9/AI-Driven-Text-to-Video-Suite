🎬 AI-Powered Audio-to-Video Synchronization

🚀 Project Overview

This project utilizes Whisper AI, MoviePy, and ImageMagick to transcribe an audio file, align the transcription with the original text, and generate a video that visually synchronizes the text with spoken words. The result is an automated video creation process where text appears dynamically based on speech timing.

✨ Features

✅ Speech-to-Text Transcription – Uses OpenAI's Whisper AI to transcribe audio files into text with timestamps.

✅ Word Alignment – Matches transcribed words to a reference text and assigns precise timing.

✅ Dynamic Text Rendering – Displays words in sync with audio using MoviePy.

✅ Custom Background & Overlays – Allows adding images, video backgrounds, and overlay text.

✅ High-Resolution Video Output – Generates professional-quality videos at 1080p.

✅ Custom Font & Styles – Fully customizable text fonts, colors, and positioning.

✅ ImageMagick Integration – Ensures high-quality text rendering using ImageMagick.

✅ Optimized Performance – Efficient text animation and video composition.

🛠️ Technologies Used

Python 3.9+

Whisper AI – Speech recognition and transcription

MoviePy – Video editing and composition

Pillow (PIL) – Image processing

ImageMagick – Text rendering for video generation

NumPy – Data processing

JSON – Data storage and alignment

FFmpeg – Video encoding and processing

📂 Project Structure

AI-StT-Align-Configurate/
│── main.py                # Main script for video generation
│── ses_dosyasi.mp3        # Input audio file
│── metin1.txt             # Reference text file
│── information.txt        # Additional text overlay
│── image.png              # Image used in the video
│── aligned_tokens.json    # Processed timestamps and text alignment
│── output_video.mp4       # Final generated video
│── requirements.txt       # Required Python dependencies
└── README.md              # This documentation file

🛠️ Installation & Setup

1️⃣ Prerequisites

Ensure you have Python 3.9+ installed. You also need FFmpeg and ImageMagick installed on your system.

Windows (FFmpeg & ImageMagick Setup)

Download FFmpeg from: https://ffmpeg.org/download.html

Install ImageMagick: https://imagemagick.org/script/download.php

Add the paths to system environment variables.

2️⃣ Install Dependencies

Clone this repository and install the required dependencies:

pip install -r requirements.txt

For ImageMagick support, ensure its path is correctly set in main.py:

os.environ["IMAGEMAGICK_BINARY"] = r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"

🚀 Usage

🎤 Step 1: Prepare Input Files

Place your audio file (ses_dosyasi.mp3) and the reference text (metin1.txt) in the project directory.

🎬 Step 2: Run the Script

Run the script to generate a synchronized video:

python main.py

📽️ Step 3: Output Video

Your final video (output_video.mp4) will be generated in the project folder.

🔥 Troubleshooting

❌ ModuleNotFoundError: No module named 'moviepy.video.fx.resize'

✅ Solution: Ensure MoviePy is properly installed:

pip install git+https://github.com/Zulko/moviepy.git@master

❌ AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'

✅ Solution: Downgrade Pillow to version 9.5.0:

pip install pillow==9.5.0

❌ [WinError 2] System cannot find the file specified (ImageMagick Error)

✅ Solution:

Ensure ImageMagick is installed and magick.exe is correctly set in os.environ.

Run in CMD: "C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe" -version to check if it's accessible.

📌 Future Enhancements

🚀 Multi-language support – Expand transcription capabilities for different languages.

🎨 Advanced text effects – Implement fade-in, animation, and motion text effects.

📹 Support for video background – Enable users to add video backgrounds instead of static colors.

🤖 AI-powered text summarization – Generate video captions automatically from summarized text.

💡 Real-time preview – Provide a real-time preview before final video rendering.

💖 Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork, create an issue, or submit a pull request. 🚀

📜 License

This project is open-source and available under the MIT License.