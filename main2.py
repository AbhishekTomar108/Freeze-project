import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QEvent
from flask import Flask
import pyautogui
import keyboard

pyautogui.FAILSAFE = False  # Disable the fail-safe mechanism

app = Flask(__name__)

class BlockInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress or event.type() == QEvent.KeyRelease:
            return True
        return super().eventFilter(obj, event)

@app.route('/')
def freeze_input():
    maxX, maxY = pyautogui.size()  # Get the maximum size of the screen
    widget = BlockInputWidget()
    widget.installEventFilter(widget)
    widget.showFullScreen()
    
    while True:
        pyautogui.moveTo(maxX/2, maxY/2)  # Move the mouse to the center of the screen

    html_response = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mouse and Keyboard Frozen</title>
    </head>
    <body>
        <h1>Mouse and Keyboard Frozen</h1>
    </body>
    </html>
    """

    return html_response

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create a QApplication instance
    app.aboutToQuit.connect(app.deleteLater)  # Connect the aboutToQuit signal to deleteLater
    window = QWidget()  # Create a QWidget instance if needed
    app.exec_()  # Enter the application event loop
    app.run(port=8002)
