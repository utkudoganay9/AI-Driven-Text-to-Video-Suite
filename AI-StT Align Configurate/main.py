import whisper
import json
from moviepy.editor import (ColorClip, AudioFileClip, TextClip,
                            CompositeVideoClip, ImageClip)
from moviepy.config import change_settings
import re
import difflib

# Specify the path where ImageMagick is installed
change_settings(
    {"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"}
)

# Load the Whisper model
model = whisper.load_model("medium")

# Specify the path to the audio file
audio_path = "ses_dosyasi.mp3"  # Your audio file name and location

# Read the original text
with open('text1.txt', 'r', encoding='utf-8') as f:
    original_text = f.read()

# Transcribe the audio to get word timestamps
result = model.transcribe(audio_path, word_timestamps=True)

audio_clip = AudioFileClip(audio_path)
video_duration = audio_clip.duration

# Video dimensions
video_width = 1920
video_height = 1080
right_column_width = 256  # Width of the right column
left_area_width = video_width - right_column_width  # Width of the left area

# Create a black background video
video_clip = ColorClip(size=(video_width, video_height), color=(0, 0, 0), duration=video_duration)

# Set audio to the video
video_clip = video_clip.set_audio(audio_clip)

# Extract transcribed words and timestamps
transcribed_words_raw = []
for segment in result['segments']:
    for word_info in segment['words']:
        word_text = word_info['word'].strip()
        if word_text != '':
            transcribed_words_raw.append({'word': word_text, 'start': word_info['start'], 'end': word_info['end']})

# Function to tokenize text with punctuation
def tokenize_with_punctuation(text):
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    return tokens

# Tokenize the original text
original_tokens = tokenize_with_punctuation(original_text)

# Tokenize the transcribed words
transcribed_tokens = [w['word'] for w in transcribed_words_raw]

# Align the tokens
matcher = difflib.SequenceMatcher(None, original_tokens, transcribed_tokens)
alignment = matcher.get_opcodes()

# Assign timestamps to original tokens
aligned_tokens = []
transcribed_index = 0

for tag, i1, i2, j1, j2 in alignment:
    if tag == 'equal':
        for idx in range(i2 - i1):
            token = original_tokens[i1 + idx]
            if transcribed_index < len(transcribed_words_raw):
                timestamp = transcribed_words_raw[transcribed_index]
                aligned_tokens.append({
                    'token': token,
                    'start': timestamp['start'],
                    'end': timestamp['end']
                })
                transcribed_index += 1
            else:
                aligned_tokens.append({'token': token, 'start': None, 'end': None})
    elif tag == 'replace':
        orig_len = i2 - i1
        trans_len = j2 - j1
        for idx in range(orig_len):
            token = original_tokens[i1 + idx]
            if transcribed_index < len(transcribed_words_raw):
                if idx < trans_len:
                    timestamp = transcribed_words_raw[transcribed_index]
                    aligned_tokens.append({
                        'token': token,
                        'start': timestamp['start'],
                        'end': timestamp['end']
                    })
                    transcribed_index += 1
                else:
                    aligned_tokens.append({'token': token, 'start': None, 'end': None})
            else:
                aligned_tokens.append({'token': token, 'start': None, 'end': None})
    elif tag == 'delete':
        for idx in range(i2 - i1):
            token = original_tokens[i1 + idx]
            aligned_tokens.append({'token': token, 'start': None, 'end': None})
    elif tag == 'insert':
        transcribed_index += (j2 - j1)

# Save aligned tokens to a JSON file
with open("aligned_tokens.json", "w", encoding="utf-8") as f:
    json.dump(aligned_tokens, f, ensure_ascii=False, indent=4)

print("Alignment of timestamps and original text completed and saved to 'aligned_tokens.json'.")

image_path = "image.png"  # Your image file name
image_width = 254
image_height = 254

image_clip = (ImageClip(image_path)
              .resize((image_width, image_height))
              .set_duration(video_duration)
              .set_position((left_area_width + (right_column_width - image_width) / 2, video_height - image_height)))

# Read text from 'information.txt' and create a TextClip
with open('information.txt', 'r', encoding='utf-8') as f:
    info_text = f.read()

info_text_clip = (TextClip(info_text, fontsize=30, color='white', font="Times-New-Roman", align='center', method='caption',
                           size=(254, None))
                  .set_duration(video_duration)
                  .set_position((left_area_width + (right_column_width - 254) / 2, 50)))  # Positioned at the top of the column

# Create the right column (transparent background)
right_column = (ColorClip(size=(right_column_width, video_height), color=(0, 0, 0, 0))
                .set_position((left_area_width, 0))
                .set_duration(video_duration))  # Added duration

# Create the red line
red_line = (ColorClip(size=(2, video_height), color=(255, 0, 0))
            .set_position((left_area_width, 0))
            .set_duration(video_duration))  # Added duration

# Adjust the text clips and their positions
text_clips = []
current_x = 50  # Starting x position (50 pixels from the left edge)
current_y = 50  # Starting y position (50 pixels from the top edge)
line_height = 50  # Line height
last_end_time = 0  # Last valid end time

# Set the maximum width and height for the text area
max_width = left_area_width - 100  # Leave a margin on the right side
max_height = video_height - 50  # Leave a margin at the bottom

# Variables to manage text overflow and resetting
overflow_time = None

for idx, token_info in enumerate(aligned_tokens):
    token = token_info['token']
    start = token_info['start']
    end = token_info['end']

    if not token or not token.strip():
        continue  # Skip empty tokens

    if start is not None and end is not None:
        duration = video_duration - start  # Set duration to the end of the video

        # Adjust current_start_time if overflow occurred
        if overflow_time is not None and start < overflow_time:
            current_start_time = overflow_time
        else:
            current_start_time = start

        # Create a temporary TextClip to get size
        try:
            temp_clip = TextClip(token, fontsize=30, color='white', font="Times-New-Roman")
        except Exception as e:
            print(f"Error creating TextClip for token '{token}': {e}")
            continue  # Skip this token on error

        token_width, token_height = temp_clip.size

        # Check if the text exceeds the maximum height
        if current_y + line_height > max_height:
            print("Maximum height reached, clearing texts and starting over.")
            overflow_time = start

            # Adjust the durations of existing text clips to end at overflow_time
            for clip in text_clips:
                clip_end = clip.start + clip.duration
                if clip_end > overflow_time:
                    clip.duration = overflow_time - clip.start

            # Reset positions
            current_x = 50
            current_y = 50

            # Continue with the current token
            current_start_time = start

        # Create the text clip and set its position and duration
        txt_clip = (temp_clip
                    .set_start(current_start_time)
                    .set_duration(duration)
                    .set_position((current_x, current_y)))

        text_clips.append(txt_clip)

        # Update positions
        current_x += token_width + 5

        # Move to next line if current_x exceeds max_width
        if current_x + token_width > max_width:
            current_x = 50  # Reset x position to the left margin
            current_y += line_height  # Move to the next line

        last_end_time = end

    else:
        # Handle tokens without timestamps (if any)
        pass

# Combine all the clips
clips = [video_clip, right_column, red_line, image_clip, info_text_clip] + text_clips
final_video = CompositeVideoClip(clips)

# Output the final video
final_video.write_videofile("output_video.mp4", fps=24)

print("Your video has been created as 'output_video.mp4'.")
