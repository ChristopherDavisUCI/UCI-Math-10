# Neural networks

## References

* Recommended video by [3Blue1Brown](https://www.youtube.com/c/3blue1brown):

<iframe width="560" height="315" src="https://www.youtube.com/embed/aircAruvnKk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* I first learned about neural networks in this online book [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) by Michael Nielsen.

* Chapter 10 of [Hands-on Machine Learning](https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ch10.html)

## Introduction

A **neural network** is a special type of function.  Here is a picture of a so-called *deep neural network*.

![Deep neural network](../images/dnn.png)

Image source: <a href="https://commons.wikimedia.org/wiki/File:Example_of_a_deep_neural_network.png">BrunelloN</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons

The left side of the picture represents the input.  The four boxes means there are four input variables/neurons/predictors/features.  

The right side of the picture represents the output, so in this case there are two outputs.  Often there may be just one output.  In the case of handwritten digits, there will be ten output neurons.

As the function is evaluated, values move from left to right.  The middle portion of the image is known as the *hidden layers* of the neural network.  When someone refers to a *deep* neural network, they are referring to the number of hidden layers; the more hidden layers, the deeper the network.

To create a neural network in Python, we will often start with `model = keras.Sequential()`.  The `Sequential` in this case refers to how the adjacent layers are connected to each other; it is also called a *feed-forward multi-layer neural network*.  There are many other types of structures also; maybe the second most famous structure is the *Convolutional Neural Network*.