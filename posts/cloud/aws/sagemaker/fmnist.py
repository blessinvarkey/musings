import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

#Image in index 0
plt.imshow(training_images[0])
#print(training_labels[0])
#print(training_images[0])

#Image in index 42
plt.imshow(training_images[42])
#print(training_labels[42])
#print(training_images[42])

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.Sequential([keras.layers.Flatten(), 
tf.keras.layers.Dense(128, activation=tf.nn.relu),
tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = tf.optimizers.Adam(), loss='sparse_categorical_crossentropy')
model.fit(training_images, training_labels, epochs = 5)

prediction = model.evaluate(test_images, test_labels)
print(prediction)

