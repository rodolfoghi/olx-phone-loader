from PIL import Image, ImageDraw, ImageFont #dynamic import
import pytesseract as ocr

ocr.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def gif_to_png(gif):
    img = Image.open(gif)
    img.save(gif+".png",'png', optimize=True, quality=70)

def image_to_text(file_name):
    phrase = ocr.image_to_string(Image.open(file_name))
    return phrase