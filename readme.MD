### CS 462 - Assignment 4. Text Clustering and Decision Trees

#### Due Oct 25, 11:59pm

_I have added optional milestone recommendations for each assignment to help you organize your time. These are just suggestions._

#### Part 1. using sklearn to do clustering.
_(Fri Mar 11)_

In this section, you'll see how to use sklearn to do K-means clustering.  There's no code to write here, but you will need
to run the algorithm with different parameters.

To begin, please take a look at [this tutorial](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html), which describes how to
do k-means using sklearn.

The modified code is in sklearn_textcluster.py.

1. **(10 points)** One purpose of this exercise is to illustrate the effectiveness of both 
TFIDF and LSA at reducing the dimensionality of the search space (and therefore the difficulty of the problem.) 

Include a plot that shows the homogeneity and completeness for no transforming, TFIDF, and LSA.

2. **(10 points)** A problem with k-means is its lack of scalability. One way to solve this is to use "minibatch". In minibatch, a subset 
of the samples in each cluster are considered in each iteration, and the centroid
is updated after each item changes clusters. This can produce faster running times.

Include a plot that compares Minibatch k-means to regular means with LSA.

3. **(10 points)** Currently we're using 4 groups out of the [20_newsgroup dataset](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html). Run an experiment that uses LSA and Minibatch
to compare the performance on:
   - These four groups (baseline)
   - 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware' (four similar groups)
   - 'rec.autos', 'alt.atheism', 'sci.space', 'talk.politics.mideast' (four different groups)
   - All 20 groups. 


#### Part 2: Decision tree 

This is the largest part of the assignment - we'll implement the basic decision tree algorithm. 
I've provided two datasets (tennis and restaurant) for you, plus some unit tests.


**(10 points)** _(Wed Mar 9)_ I've implemented entropy for you. 

Use that to implement gain. I have provided a unit test for you. 


**(10 points)**  _(Wed Mar 16)_ Use gain to implement select_attribute. Also add a unit test for select_attribute.

**(10 points)**  _(Fri Mar 18)_ Use select_attribute to implement make_tree. Add a unit test for make_tree.

**(10 points)**  _(Mon Mar 21)_ Now you are ready to implement classify. Add a unit test for this as well.

**(10 points)** _(Wed Mar 23)_ Next, measure the performance of your tree on both the restaurant and the tennis data using five-fold cross-validation. 
You should repurpose or refactor your code from assignment 3 here.

You might find that the datasets are too small to get a good measure of accuracy. One way to fix this 
is by *augmenting* the data. In this case, we'll do it by simply duplicating elements in the training set.
Try making tennis.csv and restaurant.csv contain 10 copies of each data element and see if that affects
your performance.


#### Part 3: Probability

_(Mon Mar 14)_
**(20 points)**
Please watch the Intro to Probability video and work through the questions presented in the video.
Please include a PDF in your repo with the answers to these questions.

