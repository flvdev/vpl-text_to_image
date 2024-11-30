# VPLdev Image to Text Converter

**OCR Image-to-Text Converter** é uma ferramenta simples e eficiente para converter texto contido em imagens para arquivos `.txt`. Foi projetada para ser executada localmente, sem depender de serviços online, garantindo privacidade e controle total sobre os seus dados.

---

## 🚀 **Funcionalidades**
- Processa múltiplas imagens em lote.
- Suporte a diversos formatos de imagem (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`).
- Detecta automaticamente texto em português (ou outros idiomas configurados no Tesseract OCR).
- Salva cada texto extraído em arquivos `.txt` com nomes correspondentes às imagens.

---

## 🛠️ **Pré-requisitos**
1. **Python 3.8 ou superior** instalado:
   - [Download Python](https://www.python.org/downloads/)
2. **Tesseract OCR**:
   - Faça o download e instale: [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - Certifique-se de adicionar o caminho do executável do Tesseract (`tesseract.exe`) às variáveis de ambiente do sistema.

### **Instalação das Dependências Python**
Após configurar o Python, instale as bibliotecas necessárias com:
```bash
pip install -r requirements.txt
```

---

## 📂 **Estrutura do Projeto**
```bash

vpl-text_to_image/
│
├── in/                # Coloque aqui as imagens para processamento
├── out/               # Os arquivos .txt gerados serão salvos aqui
├── main.py            # Arquivo principal para execução
├── ocr_utils.py       # Funções auxiliares (OCR e manipulação de arquivos)
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```
---

## ⚙️ **Como Usar**
・ Coloque as imagens na pasta input.
・ Execute o programa:
```bash
python main.py
・ Verifique os arquivos .txt gerados na pasta out.
```
---

## 🛡️ **Licença**
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

## 🤝 **Contribuição**
Contribuições são bem-vindas! Se você tem sugestões, melhorias ou deseja relatar um problema:

・ Faça um fork do projeto.
・ Crie uma nova branch para sua feature ou correção:
```bash
git checkout -b minha-feature
```
・ Envie seu pull request

---
## 📞 **Contato**
Se tiver dúvidas ou precisar de ajuda, entre em contato comigo através do GitHub ou envie um e-mail para contato@vpldev.tech.