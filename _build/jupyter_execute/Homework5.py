#!/usr/bin/env python
# coding: utf-8

# # Homework 5
# 
# You may submit this homework in a group of 1-3 total students.
# 
# **Due date**.  Before lecture on Friday of Week 5, October 29th.
# 
# Name(s): 
# 
# UCI ID(s): 

# ## Setup for multi-variable linear regression
# For $i = 1, 2, \ldots, m$, we have an input $\vec{x}^{\,(i)} \in \mathbb{R}^{n}$ and an output $y^{(i)} \in \mathbb{R}$.  
# 
# Given elements $\theta_0, \theta_1, \ldots, \theta_n \in \mathbb{R}$, we get a corresponding map $\mathbb{R}^n \rightarrow \mathbb{R}$ given by 
# 
# $$
# (x_1, x_2, \ldots, x_n) \mapsto \theta_0 + \theta_1 x_1 + \cdots  + \theta_n x_n.
# $$
# 
# We want to find the values of $\theta_i$ which best model $\vec{x}^{\,(i)} \leadsto y^{(i)}$.
# 
# By "best", we mean the residual sum of squares loss function is as small as possible, where the loss function is given by 
# 
# $$
# J = \frac{1}{m} \sum_{i = 1}^m \bigg(y^{(i)} - (\theta_0 + \theta_1 x_1^{(i)} + \cdots  + \theta_n x_n^{(i)})\bigg)^2.
# $$
# 
# Define an $m \times (n+1)$ matrix $X$ whose $i$-th row is $(1,  x_1^{(i)}, \ldots,  x_n^{(i)})$.  Let $\vec{y}$ denote the $m \times 1$ column vector $(y^{(1)}, \ldots, y^{(m)})^T$, and let $\vec{\theta}$ denote the $(n+1) \times 1$ column vector $(\theta_0, \theta_1, \ldots, \theta_n)^T$.
# 
# We saw on Friday that any critical point (i.e., point where the gradient is zero) would have to satisfy
# 
# $$
# -2\vec{y}^{\,T} X  + 2 \vec{\theta}^{\,T}X^T X = (0,\ldots,0),
# $$ 
# 
# which after taking transposes would imply
# 
# $$
# X^T X \vec{\theta} = X^T \vec{y}.
# $$

# ## Questions

# <p style="font-size:20px; color:blue; font-weight:bold">Question 1:</p>
# 
# (a) Geometrically, what is the meaning of $y^{(i)} - (\theta_0 + \theta_1 x_1^{(i)} + \cdots  + \theta_n x_n^{(i)})$?  Use the word *vertical* in your answer.
# 
# (b) Why do we have the $1/m$ coefficient?
# 
# (c) Would it make sense to try to maximize the loss function?  Do you think there is a maximum?
# 
# (d) When we try to minimize the loss function, some of the variables are treated as constants.  Which ones?
# 
# (e) What matrix being invertible enables us to find the critical point?  (Don't say $X$.  The matrix $X$ is usually not a square matrix, so it can't be invertible.) 

# Your answers here

# <p style="font-size:20px; color:blue; font-weight:bold">Question 2:</p>
# 
# You will need to use some NumPy linear algebra commands, for matrix multiplication, transpose, and inverse.  (Warning: you can't multiply matrices in NumPy using `*`.)
# 
# (a) Define m to be `10**5` and n to be `10**2`.  Make a matrix X as above of random real numbers uniformly distributed between 0 and 200.  Make a vector theta of length n+1 consisting of random integers between -20 and 20.  Define y to be $X \vec{\theta}$.  (So in this case the data has a perfect linear relationship, and we should be able to find theta exactly, up to some numerical precision errors.)
# 
# (b) Check if the matrix $X^T X$ is invertible.
# 
# (c) If it is invertible, check if $(X^T X)^{-1} X^T \vec{y}$ is equal to $\vec{\theta}$.

# In[1]:


# Your code here


# <p style="font-size:20px; color:blue; font-weight:bold">Question 3:</p>
# 
# How long does it take to compute $(X^T X)^{-1} X^T \vec{y}$?  What about if you multiply $m$ by 3 (but leave $n$ the same)?  What about if you multiply $n$ by 3 (but leave $m$ the same)?  Which scaling by 3 makes the bigger impact?  Do you know what part of the computation is the most difficult for the computer?

# In[2]:


# Your code here


# <p style="font-size:20px; color:blue; font-weight:bold">Question 4:</p>
# 
# Use LinearRegression from `sklearn.linear_model` to solve for theta in another way.  (You can either use `fit_intercept = False`, or you can remove the column of 1s from X.)

# In[3]:


# Your code here

