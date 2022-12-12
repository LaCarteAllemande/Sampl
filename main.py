import GUI
 
def main ():
    app = GUI.Sampl()

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        app.run()

main()

