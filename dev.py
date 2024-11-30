#              ================         +==============================                    
#               ==============             ===============================                 
#                 ============               ==========          ===========               
#                  ============               ======= ===         ===========              
#                   ============               ===== ====          ===========             
#                    ===========               === +=====           ==========             
#                     ===========              === ======           ==========             
#                     ============             += =======           =========              
#                      ===========             + ========          ==========              
#                       ===========             =========         ==========               
#                        ===========            =========       ==========                 
#                        ============           ==========   ==========                    
#                         ============         ==========+                                 
#                          ============        ==========+                                 
#                           ===========        ===========                                 
#                            ===========  +    ===========                                 
#                            ==============    ===========                 ==              
#                             ============     ===========                ===              
#                              ===========     ===========               ====              
#                               =========      ===========             ======              
#                               ========      ============           ========              
#                                ======       =============       ===========              
#                                 =====      ================  =============DEV 

# Dpendências: pip install pytesseract pillow
# Baixe e instale o Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki
# Adicione o caminho do executável do Tesseract na variável pytesseract.pytesseract.tesseract_cmd


import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract.exe'

def image_to_text(image_path, output_folder):
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image, lang='por')  # Altere o idioma conforme necessário (por, eng, etc.), para português instale o pacote adicional de linguagem

        base_name = os.path.basename(image_path).split('.')[0]
        output_file = os.path.join(output_folder, f"{base_name}.txt")
        
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(extracted_text)
        print(f"Texto extraído para: {output_file}")
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")

def process_images_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Processar
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')): # Suporte a outros formatos de imagem
            image_path = os.path.join(input_folder, file_name)
            image_to_text(image_path, output_folder)

input_folder = r"" # Pasta com as imagens
output_folder = r"" # Pasta de saída (onde os arquivos de texto serão salvos)

process_images_in_folder(input_folder, output_folder)
print("Processamento concluído!")