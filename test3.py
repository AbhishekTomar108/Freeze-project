from flask import Flask
from pynput import mouse


app = Flask(__name__)
# Create a custom mouse listener class

@app.route('/')
class MouseListener:
    def __init__(self):
        self.mouse = mouse.Controller()

    def on_move(self, x, y):
        # Restrict mouse movements to a specific area
        # Adjust the coordinates according to your desired restriction
        if x < 100 or x > 500 or y < 200 or y > 600:
            self.mouse.position = (200, 200)  # Move the mouse to a specific position

    def on_click(self, x, y, button, pressed):
        pass

    def on_scroll(self, x, y, dx, dy):
        pass

    def start(self):
        # Start listening for mouse events
        with mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()

# Create an instance of the MouseListener class and start listening
listener = MouseListener()
listener.start()


if __name__ == '__main__':
   
    app.run()