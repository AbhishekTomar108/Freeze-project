from flask import Flask, render_template
import pyautogui
import keyboard
import threading

keyboard.block_key('Win')
keyboard.block_key('tab')
keyboard.block_key('ctrl')
keyboard.block_key('enter')
keyboard.block_key('shift')
keyboard.block_key('esc')
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
keyboard.press_and_release('f11')
keyboard.block_key('f11')

pyautogui.FAILSAFE = False  # Disable the fail-safe mechanism
maxX, maxY = pyautogui.size()

app = Flask(__name__)

# def move_mouse():
#     while True:
#         pyautogui.moveTo(maxX/2, maxY/2)

@app.route('/')
def freeze_input():
    threading.Thread(target=move_mouse).start()

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
