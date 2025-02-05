import pytesseract
from PIL import Image,ImageFilter
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  
    image = image.filter(ImageFilter.SHARPEN)  
    return image

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='tur') #Enter the code of the language you want to translate, e.g. en 
    return text
