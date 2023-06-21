from flask import Flask
import pyautogui
import keyboard

pyautogui.FAILSAFE = False  # Disable the fail-safe mechanism

app = Flask(__name__)


def block_input(event):
    # Block all keyboard events by returning None
    return None


@app.route('/')
def freeze_input():
    # The stopKey is the button to press to stop. You can also use a shortcut like Ctrl+S
    maxX, maxY = pyautogui.size()  # Get the maximum size of the screen
    
    # Block the stop key from triggering events
    keyboard.hook(block_input)

    while True:
        keyboard.wait("s")
        pyautogui.moveTo(maxX/2, maxY/2)   # Wait for the stop key to be pressed
        break
        
     # Move the mouse to the center of the screen

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
