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
from ocr_utils import extrair_texto, salvar_texto, verificar_pasta

def processar_imagens(pasta_origem, pasta_destino):
    """
    Processa todas as imagens de uma pasta e salva os textos extraídos em arquivos .txt.
    """
    verificar_pasta(pasta_origem)
    verificar_pasta(pasta_destino)

    """
    Verifica se há imagens na pasta de origem
    """
    arquivos = os.listdir(pasta_origem)
    imagens = [f for f in arquivos if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]

    if not imagens:
        print("A pasta de origem está vazia ou não contém imagens suportadas.")
        return

    for imagem in imagens:
        caminho_imagem = os.path.join(pasta_origem, imagem)
        nome_base = os.path.splitext(imagem)[0]
        caminho_saida = os.path.join(pasta_destino, f"{nome_base}.txt")

        try:
            texto = extrair_texto(caminho_imagem)
            salvar_texto(texto, caminho_saida)
            print(f"Texto extraído de '{imagem}' e salvo em '{caminho_saida}'")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    """
    Configure a pasta de origem e a pasta de destino.
    """
    pasta_origem = r"./in"
    pasta_destino = r"./out"

    processar_imagens(pasta_origem, pasta_destino)
    print("Processamento concluído!")
