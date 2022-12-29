import GUI
 
from pydub import AudioSegment
import ffmpeg


def main ():
    app = GUI.Sampl()
    

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        app.run()
        # audio = AudioSegment.from_file("a.mp3", "mp3")
        # audio.export("b.mp3", format="mp3")

main()

