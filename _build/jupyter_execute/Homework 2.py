#!/usr/bin/env python
# coding: utf-8

# # UCI Math 10, Fall 2021
# 
# # Homework 2: Prime numbers, Random numbers, and Intro to pandas
# 
# To get full credit on this (and every) homework, the notebook needs to be well-organized, containing all these cells it started with, and only what is needed for you to answer the questions.
# 
# You may submit this homework in a group of 1-3 total students.
# 
# **Suggestion**.  Make a copy of this notebook, do your work in the copy, and then put your final answers in the original.
# 
# **Due date**.  Due at 11:30am on Friday of Week 2, October 8th.
# 
# <p style="font-size:20px; color:blue; font-weight:bold">Question 0:</p>
# 
# Name(s): 
# 
# UCI ID(s): 

# ## Part 1.  Prime Numbers
# 
# <p style="font-size:20px; color:blue; font-weight:bold">Question 1:</p>
# 
# If $a$ and $b$ are integers, you can check if $a$ is divisible by $b$ by computing `a%b`.  If `a%b` is equal to 0, then $a$ is divisible by $b$, otherwise, $a$ is not divisible by $b$.  Write a function `is_prime` to check if an integer is prime, using the following strategy.  (Don't use a different strategy, even if your other strategy is better!)
# 
# * The function should take one input.
# * Use the `isinstance` function to see if the input is an integer.  If it's not, return False.  (We haven't covered this function.  You can learn how it works by using help or ?.)
# * If the input is strictly less than 2, return False.
# * Using the `%` operator as described as above, check if the input is prime.  Return True if it's prime, return False otherwise.  (Reminder: an integer $p \geq 2$ is prime if its only positive divisors are $1$ and $p$.)
# * Make sure what you are returning has type bool.  (A common beginning programming mistake is to print "True" or "False", or to return the string "True" or the string "False".  Neither of those is correct.  You should be returning the Python built-in object True or False with a capital letter and no quotation marks.)

# In[1]:


def is_prime???


# <p style="font-size:20px; color:blue; font-weight:bold">Question 2</p>
# 
# Using a while loop and your is_prime function above, define a list containing the first 100 prime numbers.  (The reason a while loop is natural to use here, is because you want to keep searching until you have found 100 prime numbers.  You don't know in advance how far you need to search.)  Call the list `first_primes`.

# In[2]:


first_primes = []
while ???


# ## Part 2.  Random simulation using NumPy
# 
# The motivating question for the rest of this notebook is the following.
# 
# *  If you choose three random numbers $0 \leq x,y,z \leq 2$, what is the probability that $z > x^2 + y^2$?  
# 
# The goal of this notebook is to estimate an answer to the above question using NumPy, and then again using pandas.
# 
# Geometrically, we want to know, if we choose a point in the volume 8 cube $0 \leq x,y,z \leq 2$, what is the probability that it lies above the following paraboloid:
# 
# <img src="https://github.com/ChristopherDavisUCI/UCI-Math-10-Davis/blob/main/images/quarter_paraboloid.png?raw=true">
# 
# We will estimate a probability to this by choosing random points in this cube, and counting how many of them lie above the paraboloid.  If you want to practice your multivariable calculus skills, try to compute the exact probability (i.e., try to compute the volume of the region of the cube which lies above the paraboloid, and then divide that volume by 8, which is the total volume of the cube).

# <p style="font-size:20px; color:blue; font-weight:bold">Question 3</p>
# 
# Using [default_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng) in NumPy, create a random number generator in NumPy with the variable name rng.  See the Week 2 video "Random numbers in NumPy".

# In[3]:


# Your code here


# <p style="font-size:20px; color:blue; font-weight:bold">Question 4:</p>
# 
# Using `rng.random`, create a $10^7 \times 3$ NumPy array containing random real numbers between 0 and 2.  (Don't use any loops.  In general, we always want to avoid loops if we can, to make things faster.  `rng.random` takes a `size` input which says which shape we want to produce.)  Name the resulting array `A`.  You should think of each row of this array as corresponding to one experiment, and you should think of the three columns as corresponding to the x-value, the y-value, and the z-value.

# In[4]:


# Your code here


# <p style="font-size:20px; color:blue; font-weight:bold">Question 5:</p>
# 
# Count how many rows of A satisfy the property $x^2 + y^2 > z$.  We think of this number as the total number of "successes".  Compute "number of successes" divided by "number of experiments" to get the probability estimate.

# ## Part 3.  The same computation, but using pandas.
# 
# <p style="font-size:20px; color:blue; font-weight:bold">Question 6:</p>
# 
# Convert the above array A into a pandas DataFrame.  Name the result `df`.  Give the three columns the names x,y,z (as strings).

# In[5]:


import pandas as pd
df = ???


# <p style="font-size:20px; color:blue; font-weight:bold">Question 7:</p>
# 
# Make a new column called "above" that contains the Boolean value True if the corresponding point is above the paraboloid, and False otherwise.  You should do this without any loops.

# In[6]:


# Your code here


# <p style="font-size:20px; color:blue; font-weight:bold">Question 8:</p>
# 
# Use `.sum()` to count how many True values there are in the "above" column.  Divide by the number of rows.  Assuming you are using the numbers from A, then this should give the same probability estimate as in the previous part.

# In[7]:


# Your code here

