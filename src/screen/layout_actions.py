from PyQt6.QtWidgets import QFileDialog
from src.core.configs import ConfigManager
from src.core.downloader import DownloadWorker
from src.screen.layout import MainLayout

class LayoutActions:
    def __init__(self, layout: MainLayout, parent_widget):
        self.layout = layout
        self.parent = parent_widget
        self.config_manager = ConfigManager()
        self.download_worker = None

        self.video_qualities = ["Melhor Disponível", "1080p (Full HD)", "720p (HD)", "480p", "360p"]
        self.audio_qualities = ["Melhor Disponível", "320 kbps (Alta)", "256 kbps", "192 kbps", "128 kbps"]

        self.init_actions()

    def init_actions(self):
        # Carrega diretório salvo
        saved_folder = self.config_manager.get_download_folder()
        self.layout.folder_input.setText(saved_folder)

        # Conecta eventos de clique e alteração
        self.layout.folder_btn.clicked.connect(self.select_folder)
        self.layout.fmt_combo.currentTextChanged.connect(self.update_qualities)
        self.layout.download_btn.clicked.connect(self.start_download)

        # Inicializa lista de qualidade com o formato padrão
        self.update_qualities(self.layout.fmt_combo.currentText())

    def update_qualities(self, format_name: str):
        self.layout.quality_combo.clear()
        audio_formats = ["MP3", "OGG", "AAC"]

        if format_name in audio_formats:
            self.layout.quality_combo.addItems(self.audio_qualities)
        else:
            self.layout.quality_combo.addItems(self.video_qualities)

    def select_folder(self):
        current_folder = self.layout.folder_input.text()
        folder = QFileDialog.getExistingDirectory(self.parent, "Selecionar Pasta de Destino", current_folder)
        if folder:
            self.layout.folder_input.setText(folder)
            self.config_manager.set_download_folder(folder)

    def start_download(self):
        url = self.layout.url_input.text().strip()
        if not url:
            self.layout.status_label.setText("Cole o link do vídeo para continuar!")
            self.layout.status_label.setStyleSheet("color: #f38ba8;")
            return

        fmt = self.layout.fmt_combo.currentText()
        quality = self.layout.quality_combo.currentText()
        folder = self.layout.folder_input.text()

        self.layout.download_btn.setEnabled(False)
        self.layout.progress_bar.setValue(0)
        self.layout.status_label.setStyleSheet("color: #a6adc8;")
        self.layout.status_label.setText("Iniciando...")

        self.download_worker = DownloadWorker(url, folder, fmt, quality)
        self.download_worker.progress_signal.connect(self.update_progress)
        self.download_worker.status_signal.connect(self.update_status)
        self.download_worker.finished_signal.connect(self.on_download_finished)

        self.download_worker.start()

    def update_progress(self, val: float):
        self.layout.progress_bar.setValue(int(val))

    def update_status(self, text: str):
        self.layout.status_label.setText(text)

    def on_download_finished(self, success: bool, message: str):
        self.layout.download_btn.setEnabled(True)
        if success:
            self.layout.status_label.setStyleSheet("color: #a6e3a1;")
            self.layout.status_label.setText(message)
            self.layout.progress_bar.setValue(100)
        else:
            self.layout.status_label.setStyleSheet("color: #f38ba8;")
            self.layout.status_label.setText(message)