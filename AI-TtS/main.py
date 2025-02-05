from pdf2image import convert_from_path
from app.ocr.ocr_processor import extract_text_from_image
from app.nlp.nlp_processor import clean_text
from app.tts.tts_processor import text_to_speech
import os

def pdf_to_images(pdf_path, output_folder):
    # Poppler path way
    poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"
    # Saves each page in the PDF as an image
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    image_files = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.jpg")
        image.save(image_path, 'JPEG')
        image_files.append(image_path)
    return image_files

def main():

    script_dir = os.path.dirname(os.path.realpath(__file__))
    pdf_path = os.path.join(script_dir, "articles", "article1.pdf")

    # Save to images (article_images)
    output_folder = os.path.join(script_dir, "article_images")

    # TTS voice path (article_voice file to article_voice.mp3)
    output_audio = os.path.join(script_dir, "article_voice", "article_voice.mp3")

    print("PDF Path:", pdf_path)
    print("Output Folder:", output_folder)
    print("Output Audio:", output_audio)

    # Convert PDF to images
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_paths = pdf_to_images(pdf_path, output_folder)

    # OCR: Resimlerden metin çıkarma
    extracted_texts = []
    for image_path in image_paths:
        raw_text = extract_text_from_image(image_path)
        extracted_texts.append(raw_text)

    # Images extract to text
    full_text = " ".join(extracted_texts)
    print(f"Extracted Text: {full_text}")

    # NLP: Cleaning text
    cleaned_text = clean_text(full_text)
    print(f"Cleaned Text: {cleaned_text}")

    # TTS: Text to speech
    text_to_speech(cleaned_text, output_audio)
    print(f"Audio saved at: {output_audio}")

if __name__ == "__main__":
    main()
