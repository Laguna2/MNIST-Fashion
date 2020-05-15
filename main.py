import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = np.array(['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'])
# Normalize pixels
train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),     # input layer (1)
    keras.layers.Dense(128, activation='relu'),     # hidden layer (2)
    keras.layers.Dense(10, activation='softmax')    # output layer (3)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train
model.fit(train_images, train_labels, epochs=10)

# Evaluate model on test data
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)

print('Test accuracy:', test_acc)


# Prediction on single image
show_image = 3
prediction = model.predict(test_images)
print('Prediction on image ' + str(show_image) + ':')
index = np.argmax(prediction[show_image])
print('Image is of class: ' + class_names[index] + ', with ' + str(prediction[show_image][index]) + ' certainty')
plt.figure()
plt.imshow(test_images[show_image])
plt.show()
