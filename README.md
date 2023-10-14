# Fruits and Vegetables Image Recognition using CNN
# Data Used To Train The model
https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition

# How to launch
1. download the content and put it all in the same folder
2. you need to download/have those libraries [Tensorflow, cv2, numpy, matplotlib, tkinter, PIL]
3. Run the file Guiapp from VScode or any python code Editor
4. insert the image and press the predict button
5. Have fun and test out the pictures

# CNN Summary
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 62, 62, 32)        896       
                                                                 
 conv2d_1 (Conv2D)           (None, 60, 60, 32)        9248      
                                                                 
 max_pooling2d (MaxPooling2  (None, 30, 30, 32)        0         
 D)                                                              
                                                                 
 conv2d_2 (Conv2D)           (None, 28, 28, 64)        18496     
                                                                 
 conv2d_3 (Conv2D)           (None, 26, 26, 64)        36928     
                                                                 
 max_pooling2d_1 (MaxPoolin  (None, 13, 13, 64)        0         
 g2D)                                                            
                                                                 
 flatten (Flatten)           (None, 10816)             0         
                                                                 
 dense (Dense)               (None, 512)               5538304   
                                                                 
 dense_1 (Dense)             (None, 256)               131328    
                                                                 
 dropout (Dropout)           (None, 256)               0         
...
Total params: 5744452 (21.91 MB)
Trainable params: 5744452 (21.91 MB)
Non-trainable params: 0 (0.00 Byte)

