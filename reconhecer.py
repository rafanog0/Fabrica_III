from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time

# https://sourceforge.net/projects/tesseract-ocr-alt/

def recognize(indice_imagem):

    image_path = f"./cropped_images/screenshot_cropped_{indice_imagem}.jpeg"

    image = Image.open(image_path)

    # Converter para tons de cinza
    gray_image = image.convert('L')

    # Aumentar o contraste para melhorar a detecção
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2.0)  # Ajuste o nível conforme necessário

    # Aplicar filtro de nitidez para destacar os bordes do número
    sharpened_image = enhanced_image.filter(ImageFilter.SHARPEN)

    # Usar pytesseract para extrair apenas números
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
    number = pytesseract.image_to_string(sharpened_image, config=custom_config)

    # Limpar e exibir o número extraído
    number = number.strip()  # Remove espaços extras
    print(f"Número detectado: {number}")

i = 0

while True:
    recognize(i)
    i += 1
    time.sleep(0.5)