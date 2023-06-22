from flask import Flask, request, jsonify
from tkinter import *

import keyboard
keyboard.block_key('Win')
keyboard.block_key('tab')

keyboard.block_key('ctrl')
keyboard.block_key('enter')

win = Tk()
win.attributes('-fullscreen', True)

label= Label(win, text= "Hello World!", font=('Times New Roman bold',20))
label.pack(padx=10, pady=10)
app = Flask(__name__)

@app.route('/')
def hello():


    return "home"

if __name__ == '__main__':
 win.mainloop()
 app.run()