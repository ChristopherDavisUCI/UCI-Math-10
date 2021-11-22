# Worksheet

There is no Jupyter notebook template this week; so create a new Jupyter notebook and copy code from here as you need it.

## Imports

```
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # suppress most warnings in TensorFlow
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
```

## Recap of MNIST code

Here is the code used on Friday:

```
mnist = keras.datasets.mnist
(X_train, y_train), _ = mnist.load_data()

model = keras.Sequential(
    [
        keras.layers.InputLayer(input_shape = (28,28)),
        keras.layers.Flatten(),
        keras.layers.Dense(16, activation="sigmoid"),
        keras.layers.Dense(16, activation="sigmoid"),
        keras.layers.Dense(10,activation="softmax")
    ]
)

model.compile(
    loss="sparse_categorical_crossentropy", 
    optimizer=keras.optimizers.SGD(learning_rate=0.01),
    metrics=["accuracy"],
)

model.fit(X_train,y_train,epochs=5)
```

## Question 1

Answer the following questions related to the above code:


1. Which lines create the hidden layers?

1. Is it possible to have the same number of hidden layers, but with more weights and biases and neurons?  If so, what should be changed?  If not, why not?

1. What does the term `Dense` refer to?

1. Which line measures the performance of the neural network?

1. Which line specifies how to update the weights, in response to the measured performance?

1. Which line specifies to display extra information during training, but does not actually affect the training?

1. What number should we change if we want to take bigger steps when performing gradient descent?



## Question 2

Currently, the outputs always sum to 1 (up to rounding errors):  `model.predict(X_train[:5]).sum(axis=1)` produces 5 numbers very close to 1.  If we change the `softmax` to `sigmoid` in the output layer, what would be the possible sums of the outputs?

## A different dataset: Fashion-MNIST

Import a new dataset, specified by `fashion_mnist = keras.datasets.fashion_mnist`.

## Question 3

Display the zeroth element in the new `X_train`, using `ax.imshow` like what we did on Friday, and also check the corresponding label using `y_train`.  Does the image match the label description? [Label descriptions for Fashion-MNIST](https://keras.io/api/datasets/fashion_mnist/)

## Question 4

We will try to recognize the images in Fashion-MNIST with as high of accuracy as possible.  Even if we get 100% accuracy, it's not necessarily a good sign.  Briefly explain why.  (We'll learn a better measure, using a *test set*, later.)

## Question 5

Try to design and train a neural network that determines labels for Fashion-MNIST with over 85% accuracy.  (**Warning**.  I haven't tried to get this high of accuracy on Fashion-MNIST, but I think it should be possible.)

Some things to try:

* Use a different number of layers, or a different number neurons within each layer.

* Adjust the step size in gradient descent.

* Change the activation functions.

* Use more repetitions of the training.

* I think it is best to leave the loss as `sparse_categorical_crossentropy` and the activation function of the output layer as `softmax`, but go ahead and try changing those and let me know if they improve performance.

## Leftover material

(Not to be turned in for this worksheet.)

Here is a useful function that I don't think we've covered yet in Math 10, `np.nonzero`.

Let `A = np.array([1,0,5,10,5,8,0,5])`.   Try the commands `np.nonzero(A)` and `np.nonzero(A==5)`.

You can read about the `nonzero` function in the NumPy [documentation](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html).

I expected the following sequence of commands to produce the number `2`, but it doesn't.  How can it be changed?

```
A = np.array([1,0,5,10,5,8,0,5])
v = np.nonzero(A == 5)
v[0]
```

Here is the reason `np.nonzero` is useful in the context of Fashion-MNIST.  Imagine we want to find the first 12 sandal images (corresponding to label `5`).  We can find all of the indices for the sandal images, by using `np.nonzero` with `y_train`.  Then assuming `A` is an array of those indices (not a tuple like `np.nonzero` returns), then we can use `X_train[A[:12]]` to get the first 12 images.  The expression `X_train[A[:12]]` has shape `(12, 28, 28)`, because it is an array of 12 images, each of which is 28x28.

If you want to display these 12 images, you could put them in a 4x3 grid using Matplotlib, for example using the following code:

```
sandals = X_train[A[:12]]
fig, ax = plt.subplots(nrows=4, ncols=3)
ax_flat = ax.reshape(-1)
for i in range(12):
    ax_flat[i].imshow(sandals[i])
```