import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from GUIFunction import GFunction as GF
file_path = ""

def insert_image():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = image.resize((500, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo,)
        label.image = photo

def predict():
    global label
    s = GF(file_path)
    if hasattr(predict, "label"):
        predict.label.config(text=s,font=("Helvetica", 32))
    else:
        predict.label = tk.Label(predict_frame, text="Label in Predict")
        predict.label.pack()

# Create the main window
root = tk.Tk()
root.title("Image Viewer")
root.geometry("1000x500")

# Create a label to display the image at the top
label = tk.Label(root)
label.pack(side="top", fill="both", expand="true")

# Create a frame to hold the "Insert Image" button and "Predict" label
predict_frame = tk.Frame(root)
predict_frame.pack(side="top", pady=10)

# Create a "Predict" label (initially empty)
predict.label = tk.Label(predict_frame, text="")
predict.label.pack()

# Create an "Insert Image" button with a larger size
insert_button = tk.Button(predict_frame, text="Insert Image", command=insert_image, width=20, height=2)
insert_button.pack()

# Create a "Predict" button with a larger size
predict_button = tk.Button(root, text="Predict", command=predict, width=20, height=2)
predict_button.pack(side="top", pady=10)

# Start the main loop
root.mainloop()