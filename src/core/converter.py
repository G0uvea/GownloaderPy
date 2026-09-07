import subprocess

class MediaConverter:
    @staticmethod
    def convert_media(input_path: str, output_path: str, extra_args: list = None) -> bool:
        """
        Executa a conversão genérica utilizando o ffmpeg instalado no ambiente virtual (.venv).
        """
        cmd = ["ffmpeg", "-y", "-i", input_path]
        if extra_args:
            cmd.extend(extra_args)
        cmd.append(output_path)

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except Exception as e:
            print(f"Erro na conversão com FFmpeg: {e}")
            return False