from gtts import gTTS
import os

def text_to_speech(text, output_path):
    try:
        # Google TTS 
        tts = gTTS(text=text, lang="tr")

        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # MP3 save
        tts.save(output_path)
        print(f"Ses dosyası başarıyla kaydedildi: {output_path}")

    except Exception as e:
        print(f"Ses dönüştürme hatası: {e}")
