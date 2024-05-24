 Handwritten-Digit-Recognition

 Handwriting Recognition App

This project is a simple yet powerful handwriting recognition application built using Python, TensorFlow, and Tkinter. The app allows users to draw digits on a canvas, which are then recognized and classified using a pre-trained neural network model.

 Key Features:
- **Drawing Canvas:** A 200x200 pixel canvas where users can draw digits with their mouse. The drawn strokes are captured and displayed in real-time.
- **Handwriting Recognition:** When the user clicks the "Recognize" button, the drawn digit is processed and fed into a trained MNIST model to predict the digit.
- **Clear Canvas:** The "Clear" button allows users to reset the canvas and draw a new digit.
- **User Interface:** The app provides a simple and intuitive user interface with clear instructions and feedback on the predicted digit.

 Technical Details:
- **Model:** The app uses a convolutional neural network (CNN) model trained on the MNIST dataset, which contains 60,000 training images and 10,000 testing images of handwritten digits.
- **Libraries:** Key libraries used include TensorFlow for the neural network model, PIL (Pillow) for image processing, and Tkinter for the graphical user interface.
- **Image Processing:** The drawn image is resized to 28x28 pixels, inverted (to match the format of the training data), and normalized before being fed into the model for prediction.

This project demonstrates how machine learning can be applied to real-time image recognition tasks, providing an interactive way for users to experience the capabilities of neural networks.

