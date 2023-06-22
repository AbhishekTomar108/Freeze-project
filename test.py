from flask import Flask
import pyautogui
import keyboard

keyboard.block_key('Win')
keyboard.block_key('tab')
keyboard.block_key('ctrl')
keyboard.block_key('enter')

pyautogui.FAILSAFE = False  # Disable the fail-safe mechanism
maxX, maxY = pyautogui.size()

app = Flask(__name__)

@app.route('/')
def freeze_input():
    # The stopKey is the button to press to stop. You can also use a shortcut like Ctrl+S
    # Get the maximum size of the screen
    # Block the stop key from triggering events

    while True:
        pyautogui.moveTo(maxX/2, maxY/2)
        # Move the mouse to the center of the screen

    # Unblock the stop key
    html_response = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mouse and Keyboard Frozen</title>
    </head>
    <body>
        <h1>Mouse and Keyboard Frozen </h1>
    </body>
    </html>
    """

    return html_response

if __name__ == '__main__':
    app.run(port=8001)
