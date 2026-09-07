import json
import os

class ConfigManager:
    def __init__(self, filename: str = "config.json"):
        # Garante a criação do config.json na raiz do projeto
        core_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(core_dir, "..", ".."))

        self.filepath = os.path.join(project_root, filename)

        self.default_config = {
            "download_folder": os.path.expanduser("~/Downloads")
        }

        self.config = self.load_config()

    def load_config(self) -> dict:
        if not os.path.exists(self.filepath):
            self.save_config(self.default_config)
            return self.default_config.copy()

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, default_val in self.default_config.items():
                    data.setdefault(key, default_val)
                return data
        except Exception as e:
            print(f"Erro ao carregar configurações: {e}. Usando padrões.")
            return self.default_config.copy()

    def save_config(self, config_data: dict = None):
        if config_data is not None:
            self.config = config_data

        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(self.config, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")

    def get_download_folder(self) -> str:
        return self.config.get("download_folder", os.path.expanduser("~/Downloads"))

    def set_download_folder(self, folder_path: str):
        self.config["download_folder"] = folder_path
        self.save_config()