import numpy as np
from tensorflow.keras.models import load_model
from tkinter import *
from PIL import Image, ImageDraw, ImageOps
model = load_model('mnist_model.h5')
class HandwritingRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwriting Recognition App")
        self.canvas = Canvas(self.root, width=200, height=200, bg="white")
        self.canvas.grid(row=0, column=0, pady=10, padx=10)
        self.label = Label(self.root, text="Draw a digit", font=("Helvetica", 18))
        self.label.grid(row=1, column=0, pady=10)
        self.recognize_button = Button(self.root, text="Recognize", command=self.recognize_character)
        self.recognize_button.grid(row=2, column=0, pady=10)
        self.clear_button = Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.grid(row=3, column=0, pady=10)
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)
    def draw_on_canvas(self, event):
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)
        self.draw.line([x1, y1, x2, y2], fill="black", width=1)
    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)
    def recognize_character(self):
        resized_image = self.image.resize((28, 28))
        inverted_image = ImageOps.invert(resized_image)
        character = np.array(inverted_image)
        character = character.reshape(1, 28, 28, 1).astype('float32') / 255.0
        predictions = model.predict(character)
        prediction = np.argmax(predictions)
        self.label.config(text=f"Predicted digit: {prediction}")
if __name__ == "__main__":
    root = Tk()
    app = HandwritingRecognitionApp(root)
    root.mainloop()
