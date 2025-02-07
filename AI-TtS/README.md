```md
# 📝 **PDF to Speech Converter**
Convert your PDF documents into high-quality speech using **OCR**, **NLP**, and **TTS** technologies.

---

## 📌 **Overview**
This project extracts text from **PDF** files, processes it using **NLP**, and converts it into speech using **Google Text-to-Speech (gTTS)**. The goal is to create an automated audiobook generator from research papers, articles, or any text-based PDFs.

---

## 🚀 **Features**
- **📄 Extracts text from PDFs** using OCR.  
- **🔍 Cleans and processes text** for improved readability.  
- **🎙️ Converts text to speech (TTS)** using gTTS.  
- **🔊 Saves output** as an MP3 audio file.  
- **🖼️ Uses OCR** for scanned PDFs.

---

## 🛠️ **Technologies Used**
- **Python 3.8+**  
- **pip** (Python package manager)  
- **Poppler** (PDF handling and conversion)  
- **Tesseract OCR** (Text extraction from scanned documents)  
- **gTTS** (Google Text-to-Speech for audio generation)  

---

## 🛠️ **Installation**

### 1️⃣ **Prerequisites**
Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)

### 2️⃣ **Install Dependencies**
Run the following command to install required libraries:
```sh
pip install -r requirements.txt
```

### 3️⃣ **Install Poppler for PDF Image Conversion**

#### Windows:
- Download **Poppler for Windows** from [here](https://poppler.freedesktop.org/).
- Extract it to `C:\Program Files\poppler-xx.x.x\`.
- Add its **bin** folder to the system **PATH**.

#### Linux (Ubuntu/Debian):
```sh
sudo apt update && sudo apt install poppler-utils
```

#### MacOS (Homebrew):
```sh
brew install poppler
```

---

## 📌 **Usage**

### **Run the main script**
Execute the following command to process a PDF and generate an audio file:
```sh
python main.py
```

#### **Expected Output**
- Extracted text from PDF pages  
- Processed text  
- MP3 file saved in the **makale_sesi** directory

---

## **File Structure**
```
📂 AI-TtS
 ┣ 📂 app
 ┃ ┣ 📂 ocr          # OCR processing (image to text)
 ┃ ┣ 📂 nlp          # Text cleaning and processing
 ┃ ┣ 📂 tts          # Text-to-Speech conversion
 ┣ 📂 articles       # Folder for PDF files
 ┣ 📂 article_voice  # Folder for generated MP3 files
 ┣ 📂 article_images # Extracted images from PDFs
 ┣ 📜 main.py        # Main script
 ┣ 📜 requirements.txt  # Dependencies
 ┗ 📜 README.md      # Project documentation
```

---

## 📜 **Example Output**
```
PDF Path: articles/article1.pdf
Extracted Text: "This is an example extracted text..."
Cleaned Text: "Example cleaned text..."
Audio saved at: article_voice/article_voice.mp3
```

---

## 🛠️ **Troubleshooting**

### 1️⃣ **Poppler Not Found Error**:
- Ensure **Poppler** is installed and added to the system **PATH**.
- On Windows, add `C:\Program Files\poppler-xx.x.x\bin` to PATH.

### 2️⃣ **Tesseract OCR Not Found**:
- Install **Tesseract OCR** and add its path to `pytesseract.pytesseract.tesseract_cmd`.  
- [Download: Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

### 3️⃣ **MP3 File Not Generated**:
- Ensure you have a stable internet connection (gTTS requires online access).
- Check if the **article_audio** folder exists, or create it manually.

---

## 📌 **Contributing**
Feel free to contribute! Fork the repository, make changes, and submit a pull request. 🚀

---

## 📜 **License**
This project is licensed under the **MIT License**. See **LICENSE** for details.

---

## ⭐ **Support**
If you find this project useful, don't forget to give it a **star ⭐** on GitHub!
```
