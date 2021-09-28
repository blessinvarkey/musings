# Deep Learning Essentials 

x = 1, 2, 3, 4  
y = 1, 3, 5, 7    
Sol: y = 2x-1   

## Python API: Keras
- Keras makes it easy to define neural networks. 
- A NN is a function which can learn patterns. 
- Dense: defines a layer of connected neurons. 

### Normalizing
The process of converting an image 0-255 to 0 or 1 is called 'normalising'.

```
training_images = training_images/255
```
### Neurons

```
model = keras.Sequential([keras.layers.Dense(units=1, inputs_shape=[1])])
```

In the above example, there's only 1 dense, which means that there is only one unit, ergo there's only one neuron. 

```
model = keras.Sequential(keras.layers.Flatten(input_shape=(28,28)))
keras.layers.Dense(128, activation = tf.nn.relu)
keras.layers.Dense(10, activation=tf.nn.softmax)
```
In the above example, there's more than one neuron. The layers in sequence are part of Sequential. 
__Sequential__: Defines a SEQUENCE of layers in the neural network
__Flatten__: Flatten turns images into 1 dimentional set
__Dense__: Adds a layer of neurons
__Activation Function__: Each layer of neuron needs an activation function to tell them what to do. 
- ReLU: If x>0, return x, else return 0 - it passes values 0 or greater to the next layer in the network. 
- Softmax: takes a set of values, and effectively picks the biggest one. ex: [0.1,0.45,9] becomes [0,0,1]

- Loss functions 
- Optimizer used is Stochastic Gradient Descent

x = 1, 2, 3, 4   
y = 1, 3, 5, 7    

First guess: y = 10x-1   

```
model.compile(optimiser='sgd', loss ='mean_squared_error')
```

On making a guess, the Loss function measures the guess is, then use the optimizer and data for another guess.  

The training takes place in the fit command. 
```
model.fit(x,y, epochs=500)
```
The training value is displayed using predict() 
```
print(model.predict([10.0])) #x=10
```


