# Logistic Regression

We consider machine learning as being divided into two types of tasks:
* **Supervised learning** (example: linear regression)
* **Unsupervised learning** (example: clustering)

Within supervised learning, there are two fairly different types of problems: **regression** and **classification**.  In *regression* problems, there is a continuous quantitative value we are trying to predict.  In *classification* problems, there are discrete classes (such as Pass/No Pass or Rock/Rap/Country or UK pop/not UK pop) that we are trying to predict.

Here we will introduce logistic regression for **binary classification** problems, where there are two possible outcomes. 

```{admonition} Multi-class logistic regression
:class: info
Multi-class problems can be analyzed using the binary classification strategy also.  For example, if you want to predict whether a song is rock or rap or country, you can instead try to predict is it rock (yes or no), is it rap (yes or no), is it country (yes or no).  It's then a different question of how to combine these binary answers into an answer for the multi-class problem.
```


## References:

* [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
* Recommended video:<br> <iframe width="560" height="315" src="https://www.youtube.com/embed/zM4VZR0px8E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
* Chapter 4 of [Hands-on Machine Learning](https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ch04.html) (within Chapter 4, scroll down to the section named **Logistic Regression**).
* [Wikipedia article](https://en.wikipedia.org/wiki/Logistic_regression).  Especially the [example on the probability of passing an exam](https://en.wikipedia.org/wiki/Logistic_regression#Probability_of_passing_an_exam_versus_hours_of_study) is helpful.

## Modeling the probability

Let's use the [Wikipedia example](https://en.wikipedia.org/wiki/Logistic_regression#Probability_of_passing_an_exam_versus_hours_of_study) referenced above.
* Input variable: number of hours studied
* Output values: 0 (did not pass the exam) and 1 (passed the exam)

Instead of trying to write a function that always outputs either 0 or 1, we will write a function that tries to output the **probability** that the student passed the exam.

```{admonition} Why model probability?
:class: tip
It is better to model the probability rather than the outcome, because then we know not just the model's prediction, but also the model's confidence in that prediction.  If our model outputs 0.51, or if it outputs 0.99, both of those would get interpreted as a *pass* prediction.  But the original raw numbers 0.51 and 0.99 are more helpful, because we know to trust the *pass* prediction much more in the 0.99 case.
```

Assume there are n input variables (also called predictors or features), denoted $x_1, x_2, \ldots, x_n$.  We will model the probability using a function of the form

$$
\frac{1}{1 + e^{\theta_0 + \theta_1 x_1 + \cdots + \theta_n x_n}}
$$

The goal of linear regression is to select the best possible coefficients $\theta_0, \theta_1, \ldots, \theta_n$.

The function $1/(1 + e^{-x})$ is called the *logistic function*.  It is a good candidate for modeling probability, because its outputs are always in the correct range, between 0 and 1.

## Cost function

How do we decide what coefficients $\theta_0, \theta_1, \ldots, \theta_n$ best model the data?  We will use a cost function (or loss function), just like we did for linear regression, but we won't use the same cost function (i.e., we won't use the residual sum of squares cost function).  The smaller the value of the cost function, the better the fit.  Later we will discuss *gradient descent*, which attempts to minimize the cost function.

Say we have $m$ data points, and for each of those we have an actual output $y$, where $y$ is always $0$ or $1$.  In addition to the actual output, we have our model's output, which is a probability.  Here is a naive first guess for the cost function:

$$
\frac{1}{m} \sum_{i = 1}^m 1 - \{ \text{predicted probability of $y^{(i)}$} \}
$$

This naive cost function has the good quality that if we perfectly predict every outcome (meaning we give the actual outcome probability 1 every time), then the cost function is 0.  So the best possible predictions lead to the best possible score.  The problem is this cost function does not suitably punish predictions which are both confident and wrong.

```{admonition} Why do we need a more complicated model?
:class: warning
Imagine we are trying to model the outcome of flipping a coin.  In this case there are no input variables, and the output is either say 0 for tails or 1 for heads.  Imagine a first model that always outputs 1.  Imagine a second model that always outputs 0.5.  Clearly the second model is better, because the true probability is 0.5.  But these models would both receive the same cost value using our naive cost function from above.
```

We want to keep the good quality of the above cost function (that a perfect prediction leads to a cost of 0) while also adding in more punishment for predictions that are both confident and wrong.  Here is the model we will use, which is known as a *log-loss* cost function:

$$
\frac{1}{m} \sum_{i = 1}^m -\log\left( \text{predicted probability of $y^{(i)}$} \right)
$$

The reason people like this model is that, as the predicted probability of the actual outcome approaches 0 (as we get more and more incorrect), the cost function approaches infinity.

```{admonition} Other forms of the cost function
:class: warning
1. We had to use some plain English to describe our cost function.  Usually you will see this function written entirely in variables, which makes it look more complicated.  The reason is because the formula looks different based on whether $y^{(i)}$ is 0 or 1.

2.  scikit-learn by default uses a more fancier version of this cost function, which includes some additional component called *regularization*.  Regularization is a useful technique that can help to avoid over-fitting, but I don't think we will discuss it in Math 10.
```

 