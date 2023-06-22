from flask import Flask
import pyautogui
import keyboard

pyautogui.FAILSAFE = False  # Disable the fail-safe mechanism

app = Flask(__name__)

@app.route('/')
def freeze_input():
    stopKey = "s"  # The stopKey is the button to press to stop. You can also use a shortcut like Ctrl+S
    maxX, maxY = pyautogui.size()  # Get the maximum size of the screen
    
    while True:
        if keyboard.is_pressed(stopKey):
            break
        else:
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
    app.run(port=8001)