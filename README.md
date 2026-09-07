# GownloaderPy 🎵🎬

O **GownloaderPy** é uma aplicação desktop leve, moderna e intuitiva para download e conversão de vídeos e áudios da internet, desenvolvida em Python com PyQt6.

---

## 🚀 Funcionalidades

- 📥 **Download de Mídia:** Suporte a vídeos e áudios de diversas plataformas via `yt-dlp`.
- 🎼 **Conversão Automática:** Exportação direta para formatos como **MP4, MOV, AV1, MP3, OGG e AAC**.
- ⚙️ **Seleção de Qualidade:** Opções dinâmicas de resolução para vídeo (até 1080p Full HD) e bitrate para áudio (até 320 kbps).
- 📁 **Gerenciamento de Pastas:** Escolha onde salvar seus arquivos com persistência das configurações em `config.json`.
- ⚡ **Execução Assíncrona:** Downloads em segundo plano (`QThread`) mantendo a interface sempre responsiva.
- 🎨 **Interface Catppuccin Mocha:** Design escuro moderno com alto contraste e barra de progresso visual.

---

## 🛠️ Estrutura do Projeto

```text
GownloaderPy/
├── README.md   # Documentação do projeto
└── src/
    ├── main.py     # Ponto de entrada da aplicação
    ├── core/
    │   ├── configs.py      # Gerenciador do arquivo config.json
    │   ├── converter.py    # Funções auxiliares para conversão/FFmpeg
    │   └── downloader.py   # Worker em QThread com yt-dlp
    └── screen/
        ├── layout.py           # Estruturação e interface estática dos widgets
        ├── layout_actions.py   # Lógica de eventos, sinais e threads
        ├── style.qss           # Estilização visual (CSS/QSS Catppuccin)
        └── window.py           # Janela principal da aplicação