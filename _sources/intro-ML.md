# Introduction to Machine Learning

We give a brief introduction to machine learning, and to some of the most commonly used terms in the subject.  Much of the material on this page is vague and not precisely defined.  Things will become more precise when we discuss specific examples of machine learning algorithms, like linear regression.

To define machine learning, we will use this quote from *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd Edition*, by Aurélien Géron:

* **Machine Learning** is the science (and art) of programming computers so they can learn from data.

The reason for the word *learning* is that, as more data is provided, the algorithm can update (and hopefully become more accurate).  This updating is what is meant by learning.

## Supervised vs unsupervised learning

There are two basic categories of machine learning: supervised learning, and unsupervised learning.  In **supervised learning**, there is some specific quantity (or label) that is trying to be assigned, while in **unsupervised learning**, there isn't.  The reason for the names is that, with supervised learning, the algorithm is trained using labeled data.  The algorithm receives *supervision* in the form of correct answers for some of the data.  An algorithm for unsupervised learning will also receive data, but it is unlabeled data.

The most fundamental example of supervised learning is **linear regression**.  With regards to linear regression, we are provided with one or more input variables $X$, which are traditionally called *predictors*, and an output variable $y$, called the target, and we try to model the target as a linear (plus a constant) function of the input variables.

The most famous example of unsupervised learning is **clustering**, where we feed in data and the algorithm is supposed to divide that data into different clusters.  We do not provide any initial labels (for example, we don't say something like, "these points should be in cluster 1, while these others should be in cluster 2").  That is the sense in which this would be an unsupervised learning algorithm.

## Regression vs classification

Within the supervised learning category, there is a further important distinction between regression problems and classification problems.  In a **regression** problem, the target is assumed to be some continuous quantitative value.  (Even if the target is something like "number of deaths", I would still count that as a regression problem.  It might not be continuous in the sense that there can never be a fractional death, but there is still a clear ordering and if our model outputs something like 100.4 deaths, that is natural enough to interpret.)

In a **classification** problem, the target is assumed to take values in some discrete set of categories.  For example, if we are trying to predict the musical genre of a song, this would be thought of as a classification problem.