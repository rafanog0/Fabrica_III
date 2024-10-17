import win32gui
import win32ui
import win32con
import time
import os
from PIL import Image

def background_screenshot_and_crop(hwnd, count):
    # Obter o tamanho total da janela
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    # Coordenadas do corte baseadas em porcentagem da janela
    crop_left_pct = 0.77  
    crop_top_pct = 0.895   
    crop_right_pct = 0.798
    crop_bottom_pct = 0.93 

    # Calcula as coordenadas de corte reais em pixels
    crop_left = int(width * crop_left_pct)
    crop_top = int(height * crop_top_pct)
    crop_right = int(width * crop_right_pct)
    crop_bottom = int(height * crop_bottom_pct)
    crop_width = crop_right - crop_left
    crop_height = crop_bottom - crop_top

    # Ajustar coordenadas para o corte no momento da captura
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, crop_width, crop_height)
    cDC.SelectObject(dataBitMap)

    # Realiza a captura diretamente na área cortada
    cDC.BitBlt((0, 0), (crop_width, crop_height), dcObj, (crop_left, crop_top), win32con.SRCCOPY)

    # Cria a pasta "cropped_images" se não existir
    output_dir = "cropped_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Salva a imagem cortada diretamente na pasta "cropped_images"
    cropped_image_path = f"{output_dir}/screenshot_cropped_{count}.jpeg"
    dataBitMap.SaveBitmapFile(cDC, cropped_image_path)

    # Limpar recursos
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    print(f"Imagem cortada salva em: {cropped_image_path}")

# Definir o identificador da janela
hwnd = win32gui.FindWindow(None, "cardioEmotion Home")

# Loop para tirar screenshots periodicamente e salvar apenas a área cortada
i = 0
try:
    while True:
        background_screenshot_and_crop(hwnd, i)
        i += 1
        time.sleep(0.2) 
except KeyboardInterrupt:
    print("Captura de tela periódica interrompida.")
