import os

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.screen.layout import MainLayout
from src.screen.layout_actions import LayoutActions

WINDOW_SIZE = (560, 420)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_window()

        # Instancia Layout e vincula as Ações
        self.main_layout_ui = MainLayout(self)
        self.actions = LayoutActions(self.main_layout_ui, self)

        # Adiciona o Layout na janela
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.main_layout_ui)

        # Carrega o estilo
        base_path = os.path.dirname(os.path.abspath(__file__))
        qss_path = os.path.join(base_path, "style.qss")
        self.load_stylesheet(qss_path)

    def setup_window(self):
        self.setWindowTitle("RIPPERA")
        self.setFixedSize(WINDOW_SIZE[0], WINDOW_SIZE[1])

        screen_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(screen_dir, "..", ".."))
        icon_path = os.path.join(project_root, "icon.ico")

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Aviso: Ícone não encontrado em {icon_path}")

    def load_stylesheet(self, qss_path: str):
        if os.path.exists(qss_path):
            with open(qss_path, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())