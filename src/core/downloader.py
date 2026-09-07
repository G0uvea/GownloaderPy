import os
import re
from PyQt6.QtCore import QThread, pyqtSignal
import yt_dlp

class DownloadWorker(QThread):
    progress_signal = pyqtSignal(float)
    status_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, url: str, folder: str, fmt: str, quality: str):
        super().__init__()
        self.url = url
        self.folder = folder
        self.fmt = fmt.lower()
        self.quality = quality

    def run(self):
        try:
            self.status_signal.emit("Obtendo informações da mídia...")

            ydl_opts = {
                'outtmpl': os.path.join(self.folder, '%(title)s.%(ext)s'),
                'progress_hooks': [self._progress_hook],
                'nocheckcertificate': True,
                'no_warnings': True,
                'extractor_args': {'youtube': ['player_client=android,tv,web']},
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            }

            audio_formats = ["mp3", "ogg", "aac"]

            if self.fmt in audio_formats:
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': self.fmt,
                        'preferredquality': self._parse_audio_quality(self.quality),
                    }],
                })
            else:
                height = self._parse_video_quality(self.quality)
                if height:
                    ydl_opts['format'] = f'bestvideo[height<={height}]+bestaudio/best'
                else:
                    ydl_opts['format'] = 'bestvideo+bestaudio/best'

                ydl_opts['merge_output_format'] = self.fmt

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])

            self.finished_signal.emit(True, "Download concluído com sucesso!")

        except Exception as e:
            self.finished_signal.emit(False, f"Erro no download: {str(e)}")

    def _progress_hook(self, d: dict):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded_bytes = d.get('downloaded_bytes', 0)

            if total_bytes > 0:
                percent = (downloaded_bytes / total_bytes) * 100
                self.progress_signal.emit(percent)
                self.status_signal.emit(f"Baixando... {percent:.1f}%")
            else:
                self.status_signal.emit("Baixando...")

        elif d['status'] == 'finished':
            self.status_signal.emit("Processando e convertendo arquivo...")

    def _parse_video_quality(self, quality_text: str) -> str:
        match = re.search(r'(\d+)p', quality_text)
        return match.group(1) if match else None

    def _parse_audio_quality(self, quality_text: str) -> str:
        match = re.search(r'(\d+)', quality_text)
        return match.group(1) if match else '192'