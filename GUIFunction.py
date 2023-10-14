import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np

def GFunction(image_path):
    cnn = tf.keras.models.load_model('trained_model.h5')
    img = cv2.imread(image_path)
    plt.imshow(img)
    plt.title('Test Image')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    #converting
    image = tf.keras.preprocessing.image.load_img(image_path,target_size=(64,64)) #resize the image
    input_arr=tf.keras.preprocessing.image.img_to_array(image) #convert to input array 
    input_arr = np.array([input_arr]) #converting single image to batch
    prediction = cnn.predict(input_arr)
    #checking
    result_index = np.where(prediction[0] == max(prediction[0]))
    class_names = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']
    s = '{}'.format(class_names[result_index[0][0]]).capitalize()
    return s