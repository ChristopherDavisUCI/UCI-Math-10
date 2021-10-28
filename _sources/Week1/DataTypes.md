---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Data types in Python

There are a huge number of data types in Python, both built-in data types (like list) and data types that come from an external library (like NumPy arrays).  Often data types can appear quite similar.  Here is an example of five data types which all share some common properties:
* list
* set
* tuple
* range
* NumPy array

It is important to recognize in what ways these are similar and in what ways they are different.  Understanding the pros and cons of different data types is essential to selecting the data type which is best-suited for a given task.

+++

## list

One of the most fundamental data types in Python is type *list*.

```{code-cell} ipython3
my_list = [3,1,4,1,5]
```

```{code-cell} ipython3
type(my_list)
```

```{code-cell} ipython3
len(my_list)
```

Notice that the following probably doesn't produce what you expect.  The reason is that indexing in Python starts at 0, not at 1.

```{code-cell} ipython3
# indexing
my_list[2]
```

```{code-cell} ipython3
# indexing
my_list[0]
```

If you remember the colon operator from Matlab, then the following, which is known as *slicing*, should look familiar.

```{code-cell} ipython3
# slicing
my_list[2:]
```

One difference from Matlab is that the right-endpoint is usually not included by default in Python.  For example, the following code `my_list[2:4]` produces a list that contains `my_list[2]` and `my_list[3]` but does not contain `my_list[4]`.

```{code-cell} ipython3
my_list[2:4]
```

```{code-cell} ipython3
my_list
```

```{code-cell} ipython3
my_list[2] = "hello Math 10"
```

```{code-cell} ipython3
my_list
```

```{code-cell} ipython3
# this changes my_list
my_list.append(4)
```

```{code-cell} ipython3
my_list
```

```{code-cell} ipython3
new_list = [3,1,4,1]
```

A common cause of mistakes is thinking that a command will change a structure, when in fact it has no effect on the original object.  In the following code, `sorted(new_list)` doesn't change `new_list`.  It makes a different list.

```{code-cell} ipython3
# has no effect on new_list
sorted(new_list)
```

```{code-cell} ipython3
new_list
```

If we wanted to actually replace `new_list` with a sorted version of `new_list`, we should use a syntax like the following.

```{code-cell} ipython3
# to change the original
new_list = sorted(new_list)
```

```{code-cell} ipython3
new_list
```

```{code-cell} ipython3
new_list.extend([3,1,4])
```

```{code-cell} ipython3
new_list
```

```{code-cell} ipython3
new_list.append([3,1,4])
```

```{code-cell} ipython3
new_list
```

```{code-cell} ipython3
new_list[-1]
```

```{code-cell} ipython3
type(new_list[-1])
```

```{code-cell} ipython3
type(new_list[-2])
```

## set
A set in Python is similar to a list in many ways.  For example, it contains a collection of objects.  Some differences are that sets do not have an order, and sets cannot have repeated elements.  Also sets are more limited in terms of the types of objects they can contain.

We start by viewing the list `my_list`.

```{code-cell} ipython3
my_list
```

Here is the standard way to convert data types in Python.  In this case, we are converting from a list to a set.

```{code-cell} ipython3
my_set = set(my_list)
```

```{code-cell} ipython3
my_set
```

```{code-cell} ipython3
type(my_set)
```

Notice how the square brackets `[...]` got replaced by curly brackets `{...}` and how the order changed and the repetitions disappeared.

```{code-cell} ipython3
set([3,1,4,1,-10,5])
```

Sets don't have a notion of order, so taking the 2nd element doesn't make sense.

```{code-cell} ipython3
my_set[2]
```

```{code-cell} ipython3
len(my_set)
```

```{code-cell} ipython3
my_set
```

Here is the by-hand way to make a set (as opposed to converting from a list).

```{code-cell} ipython3
{2,10,4}
```

## tuple
In simple cases, a tuple is almost indistinguishable from a list.  The only real difference in the following first few examples is that the tuple has round parentheses instead of square brackets.

```{code-cell} ipython3
my_tuple = (3,1,4,1)
```

```{code-cell} ipython3
my_tuple
```

```{code-cell} ipython3
my_tuple[2]
```

```{code-cell} ipython3
my_tuple[1:3]
```

```{code-cell} ipython3
len(my_tuple)
```

If we want to convert a tuple into a list, we can do that by wrapping the variable name inside of `list`, as in this example.  The first line makes the conversion, and the second line displays the result.

```{code-cell} ipython3
my_list = list(my_tuple)
my_list
```

How are tuples different from lists?  Here is one example.  You should not change a tuple after you've created it.

```{code-cell} ipython3
print("hi")
my_tuple[2] = 10
print("hello")
```

Another example of how you should not change a tuple:

```{code-cell} ipython3
my_tuple.append(4)
```

Why would we ever use tuples?  One pragmatic advantage of a tuple over a list is that a tuple can (usually) go in a set, while a list can't.

```{code-cell} ipython3
# Why would we ever use tuples?
# tuples can go in a set, and lists can't
{5,10,my_tuple}
```

```{code-cell} ipython3
{5,10,my_list}
```

Another practical reason tuples are important is that, when you are using Python code written by someone else, it will often involve tuples.  Here is a small example and a preview of the NumPy arrays discussed below.

```{code-cell} ipython3
import numpy as np
A = np.array(my_list)
A
```

The variable `A` represents a NumPy array.

```{code-cell} ipython3
type(A)
```

NumPy arrays have a `shape` attribute which tells us the dimensions of the array.  (That is especially useful if `A` represents a matrix.)

```{code-cell} ipython3
A.shape
```

This `shape` attribute is represented as a tuple.

```{code-cell} ipython3
type(A.shape)
```

Here is a discussion of differences between lists and tuples from [Stack Overflow](https://stackoverflow.com/a/626871), although that discussion, like many discussions on Stack Overflow, is a little advanced for us as we're just beginning with Python.

## range
We won't use `range` by itself very often, but we will use it all the time to produce repetitions, such as during a for loop.  The `range` function is similar to how `:` works in Matlab, although with range, the step-size goes at the end, rather than in the middle.

```{code-cell} ipython3
my_range = range(0,100,3)
```

```{code-cell} ipython3
my_range
```

This element `my_range` is yet another type in Python.

```{code-cell} ipython3
type(my_range)
```

```{code-cell} ipython3
list(my_range)
```

```{code-cell} ipython3
list(range(0,10,1))
```

```{code-cell} ipython3
list(range(10))
```

You are not allowed to use range with non-integer entries.
```{code-cell} ipython3
range(0,10,0.5)
```

One reason range is useful is it can represent gigantic pieces of data without actually taking up much space in memory.  In the following, we want to write $10^{40}$, which in Python is expressed using `10**40` (the caret symbol `^` means something else in Python).


```{code-cell} ipython3
my_range = range(0,10**40,3)
```

It would be a very bad idea to try to convert that into a list, because no computer can store $10^{40}$ distinct integers.

```{code-cell} ipython3
list(range(0,10**40,3))
```

Even though `my_range` doesn't literally contain all of those numbers, Python is still smart enough to answer some basic questions about `my_range`.  For example:

* Is 252523525252421 in `my_range`?

```{code-cell} ipython3
252523525252421 in my_range
```

What about 252523525252422?

```{code-cell} ipython3
252523525252422 in my_range
```

* What are the last 4 elements in my_range?

```{code-cell} ipython3
my_range[-4:]
```

By default, those 4 elements are also represented as a range object.  We can explicitly convert that range object to a list.

```{code-cell} ipython3
list(my_range[-4:])
```

## NumPy arrays
All of the above data types are part of standard Python.  Often in Math 10, we will instead be working with data types defined in separate Python libraries.  *NumPy* is probably the library we will use second-most often (behind only *pandas*).

Here is the syntax for importing NumPy.  There is a standard abbreviation `np` which should always be used when referring to this library.

```{code-cell} ipython3
import numpy as np
```

We saw above that `range` cannot be used with non-integer values.  (These decimal numbers are called *floats* in Python.)

```{code-cell} ipython3
step = 0.5
type(step)
```

```{code-cell} ipython3
range(0,10,step)
```

NumPy defines a similar function called `arange` which can work with floats.  The following though does not work.

```{code-cell} ipython3
arange(0,10,step)
```

The reason `arange(0,10,step)` does not work is that Python does not know that `arange` is defined by NumPy.  To tell Python where to look for the definition, we use the syntax `np.arange`.

```{code-cell} ipython3
A = np.arange(0,10,step)
A
```

```{code-cell} ipython3
type(A)
```

NumPy arrays are the last data type we will consider in this notebook.  Recall the following syntax for turning `my_tuple` into a list:

```{code-cell} ipython3
list(my_tuple)
```

There is the same sort of syntax for turning `my_tuple` into a NumPy array:

```{code-cell} ipython3
A = np.array(my_tuple)
A
```

```{code-cell} ipython3
type(A)
```

Slicing works with NumPy arrays:
```{code-cell} ipython3
A[1:]
```

There are many NumPy functions which can be applied very efficiently to every element in a NumPy array.  Here is an example of applying cosine to every entry in `A`:
```{code-cell} ipython3
np.cos(A)
```

We will see later examples of how to time operations in Python, and then we will see concretely that many mathematical operations are much faster when performed on a NumPy array than when performed on something like a list or tuple.

