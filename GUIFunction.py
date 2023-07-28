import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np

def GFunction(image_path):
    #testing set
    test_set = tf.keras.utils.image_dataset_from_directory(
    'G:\\Fruit and veg\\Fruit_recognition\\archive (1)\\test',
    labels='inferred',  #labels are generated from the directory structure
    label_mode='categorical', #means data can be anything img,strings,etc encode as a categorical vector
    class_names=None, #to control order
    color_mode='rgb', #type of image color
    batch_size=32, #the number of samples  to estimate the error gradient before the model weight are updated
    image_size=(64, 64), #image size pixel x pixel
    shuffle=True, #select samples at random
    seed= None, #to save the seed of model so it can produce same result
    validation_split= None, #to split data for validation
    subset= None, #this return dataset of training data or validation data or both if validation is set
    interpolation='bilinear', #to estimate the values of unknown data points that fall in between existing, known data points.
    follow_links=False, #if you want to follow other links
    crop_to_aspect_ratio=False #will change the aspect ratio of an image if it doesn't match the targeted images ratio (when True)
)
    cnn = tf.keras.models.load_model('G:\\Fruit and veg\\Fruit_recognition\\trained_model.h5')
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
    s = 'It\'s a {}'.format(test_set.class_names[result_index[0][0]])
    return s