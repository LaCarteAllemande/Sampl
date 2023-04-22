import MainWindow
 
from pydub import AudioSegment
import ffmpeg


def main ():
    app = MainWindow.MainWindow()
    

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        app.run()

main()

