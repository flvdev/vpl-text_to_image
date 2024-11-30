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
#                                 =====      ================  =============DEV | https://github.com/flvdev/vpl-text_to_image

# Dpendências: pip install pytesseract pillow
# Baixe e instale o Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki
# Adicione o caminho do executável do Tesseract na variável pytesseract.pytesseract.tesseract_cmd

import os
from PIL import Image
import pytesseract

"""
Configure o caminho do executável do Tesseract OCR.
"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto(imagem_path):
    """
    Extrai texto de uma imagem usando Tesseract OCR.
    """
    try:
        imagem = Image.open(imagem_path)
        texto = pytesseract.image_to_string(imagem, lang='por')   # Altere o idioma conforme necessário (por, eng, etc.), para português instale o pacote adicional de linguagem
        return texto
    except Exception as e:
        raise RuntimeError(f"Erro ao processar a imagem '{imagem_path}': {e}")

def salvar_texto(texto, arquivo_saida):
    """
    Salva o texto extraído em um arquivo .txt.
    """
    try:
        with open(arquivo_saida, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar o texto no arquivo '{arquivo_saida}': {e}")

def verificar_pasta(pasta):
    """
    Verifica se a pasta existe e cria a pasta caso não exista..
    """
    if not os.path.exists(pasta):
        os.makedirs(pasta)