from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QProgressBar, QVBoxLayout, QHBoxLayout, QFrame
)

class MainLayout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(16)
        main_layout.setContentsMargins(24, 24, 24, 24)

        # 1. URL SECTION
        url_layout = QVBoxLayout()
        url_label = QLabel("URL do Vídeo / Áudio:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Cole o link aqui...")
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        main_layout.addLayout(url_layout)

        # 2. DESTINATION SECTION
        folder_layout = QVBoxLayout()
        folder_label = QLabel("Salvar em:")
        folder_input_layout = QHBoxLayout()

        self.folder_input = QLineEdit()
        self.folder_input.setReadOnly(True)

        self.folder_btn = QPushButton("Selecionar")
        self.folder_btn.setObjectName("btn_pasta")
        self.folder_btn.setFixedHeight(34)
        self.folder_btn.setFixedWidth(100)

        folder_input_layout.addWidget(self.folder_input)
        folder_input_layout.addWidget(self.folder_btn)
        folder_layout.addWidget(folder_label)
        folder_layout.addLayout(folder_input_layout)
        main_layout.addLayout(folder_layout)

        # 3. OPTIONS SECTION (Format and Quality)
        options_layout = QHBoxLayout()

        fmt_layout = QVBoxLayout()
        fmt_label = QLabel("Formato:")
        self.fmt_combo = QComboBox()
        self.fmt_combo.addItems(["MP4", "MOV", "AV1", "MP3", "OGG", "AAC"])
        fmt_layout.addWidget(fmt_label)
        fmt_layout.addWidget(self.fmt_combo)

        quality_layout = QVBoxLayout()
        quality_label = QLabel("Qualidade / Resolução:")
        self.quality_combo = QComboBox()
        quality_layout.addWidget(quality_label)
        quality_layout.addWidget(self.quality_combo)

        options_layout.addLayout(fmt_layout)
        options_layout.addLayout(quality_layout)
        main_layout.addLayout(options_layout)

        # Divider Line
        divider = QFrame()
        divider.setObjectName("divisor")
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(divider)

        # 4. DOWNLOAD BUTTON
        self.download_btn = QPushButton("Iniciar Download")
        self.download_btn.setFixedHeight(42)
        main_layout.addWidget(self.download_btn)

        # 5. PROGRESS BAR AND STATUS
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(18)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)

        self.status_label = QLabel("Pronto para baixar")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.status_label)