from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time

# https://sourceforge.net/projects/tesseract-ocr-alt/

def recognize(indice_imagem):

    image_path = f"./cropped_images/screenshot_cropped_{indice_imagem}.jpeg"

    image = Image.open(image_path)

    # Aumentar o contraste para melhorar a detecção
    enhancer = ImageEnhance.Contrast(image)
    
    enhanced_image = enhancer.enhance(2.0)

    # Aplicar filtro de nitidez para destacar os bordes do número
    sharpened_image = enhanced_image.filter(ImageFilter.SHARPEN)

    # Converter tudo que não é branco em preto
    # Pixels com valor 255 permanecem, o restante é convertido para 0
    binary_image = sharpened_image.point(lambda x: 255 if x == 255 else 0)
    
    new_size = (binary_image.width * 4, binary_image.height * 4)  # Dobrar o tamanho, por exemplo

    resized_image = binary_image.resize(new_size, Image.BICUBIC)
    #save imagem for debugging

    # resized_image.save(f"./imagens/screenshot_cropped_binary_{indice_imagem}.jpeg")


    # Usar pytesseract para extrair apenas números
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
    number = pytesseract.image_to_string(resized_image, config=custom_config)

    # Limpar e exibir o número extraído
    number = number.strip()  # Remove espaços extras
    print(f"Número detectado: {number}")

i = 0

while True:
    recognize(i)
    i += 1
    time.sleep(0.5)
