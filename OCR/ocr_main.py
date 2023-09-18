# Download Pytesseract:
# https://github.com/UB-Mannheim/tesseract/wiki

from PIL import Image
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image using Pillow (PIL)
image_path = './image-3.jpg'

img = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(img)
print(text)

# Save the text into File
output_file_path = 'extracted_text.txt'

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(text)

print(f'Text saved to {output_file_path}')
