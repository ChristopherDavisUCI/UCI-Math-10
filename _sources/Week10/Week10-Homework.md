# Homework

## Gradient descent

The first part of the homework is about gradient descent.  We will practice using gradient descent with the two-variable function $f(x,y) = \frac{x^2}{4} + y^2$.

Here is an example of plotting conour lines using Matplotlib.  (Adapted from [Density and Contour Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html).)

```
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (x**2)/4 + y**2

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, 10, cmap='Greys');
```

## Question 1
Try to make the plot look better:
* Try adding `plt.style.use('???')`, where `???` gets replaced by one of the choices from `plt.style.available`.
* Change `cmap='Greys'` to use a more interesting color map.  You can find options in the [Matplotlib documentation](https://matplotlib.org/stable/tutorials/colors/colormaps.html).

## Question 2
Math 2D review: what is the relationship between gradient and contour lines?  (When you perform the gradient descent below, you should look at the contour plot and make sure your directions seem correct.)

## Question 3

Perform gradient descent by hand, starting at the initial point $(4,4)$ and using a step size (or learning rate) of 0.01.  Where do you land after one step?  After two steps?  Repeat this for a step size of 1, and a step size of 10.  (Your answer for this question should be six total points: two points for each step size.  Always begin at the point (4,4).  You'll definitely want to use a calculator.)

## Neural networks and over-fitting

The second part of this homework is to practice with neural networks using the dataset for your final project.

## Question 4
Train a neural network using the dataset for your final project.  Clearly describe in a markdown cell what you are trying to compute.  

(In class, we have only done examples with *classification*.  If you only have numbers but want to do classification, one easy way is to add a column which is something like, "True or False: this value is bigger than 8."  Another option is to use a neural network for *regression*, the main difference is you should change the [loss function](https://keras.io/api/losses/) to something more well-suited to regression, and the activation function of the output layer to something that has the correct range.  One option for the activation function in the output layer is to simply not specify anything; I think that should work.  If it doesn't work, try specifying `linear`, which means not to use any activation function.)

## Question 5
Show a plot of the training loss and the validation loss, like what we did in class on Wednesday.

## Question 6
Based on the plot, do you think you were over-fitting the data?

## Question 7

In the gradient descent part, we were using gradient descent to try to find a minimum of a two-variable function.  In this part, how many variables are there for the function we are trying to minimize?  (Hint.  Use `model.summary()`.  You shouldn't have to make any calculations yourself.)