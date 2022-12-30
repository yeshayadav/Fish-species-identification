import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

from keras.models import load_model

model = load_model('model_inception.h5')
from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array


top = tk.Tk()
top.geometry('800x600')
top.title('Fish Breed Prediction  using inception V3')
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    test_image = load_img(file_path, target_size=(224, 224))  # load image
    print("@@ Got Image for prediction")

    test_image = img_to_array(test_image) / 255  # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis=0)  # change dimention 3D to 4D

    result = model.predict(test_image).round(3)  # predict diseased palnt or not
    print('@@ Raw result = ', result)

    pred = np.argmax(result)  # get the index of max value

    if pred == 0:
        print("Black Sea Sprat")
        label.configure(foreground='#011638', text="Black Sea Sprat")
    elif pred == 1:
        print('Gilt Head Bream'),
        label.configure(foreground='#011638', text="Gilt Head Bream")
    elif pred == 2:
        print('Hourse Mackerel'),
        label.configure(foreground='#011638', text='Hourse Mackerel')
    elif pred == 3:
        print('Red Mullet'),
        label.configure(foreground='#011638', text="Red Mullet")
    elif pred == 4:
        print('Red Sea Bream'),
        label.configure(foreground='#011638', text="Red Sea Bream")
    elif pred == 5:
        print('Sea Bass'),
        label.configure(foreground='#011638', text='Sea Bass')
    elif pred == 6:
        print('Shrimp'),
        label.configure(foreground='#011638', text='Shrimp')
    elif pred == 7:
        print('Striped Red Mullet'),
        label.configure(foreground='#011638', text='Striped Red Mullet')
    elif pred == 8:
        print('Trout'),
        label.configure(foreground='#011638', text='Trout')
    
    
    



def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image",
                        command=lambda: classify(file_path),
                        padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25),
                            (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Fish Breed Predictor", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
