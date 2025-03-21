import pandas as pd
import math
from collections import Counter

def ZeroR(data) :
    c = Counter(data)
    return c.most_common(1)[0][0]

class Node :
    def __init__(self, classification=None,attribute=None):
        self.classification = classification
        self.attribute = attribute
        self.children = {}

    def isLeaf(self):
        return len(self.children) == 0

# assume that s is a pandas series.
# return the entropy of the series
def entropy(s) :
    counts = s.value_counts()
    e = sum([item / sum(counts) * math.log(item / sum(counts), 2) * -1 for item in counts])
    return e

# gain takes two inputs: a Series containing
# the feature (such as outlook) and a Series
# containing the classification such as 'play'.
# gain should compute the entropy for each feature value and then return
# their weighted average.

def gain(features, classifications) :
    vars = set(features)
    indep_vars = list(features)
    dep_vars = list(classifications)
    initial_entropy = entropy(classifications)
    # you do the rest


# select_attribute takes two inputs:
# 1. A dataframe consisting of the features to be considered
# 2. A Series containing the corresponding classifications.
# select_attribute computes the gain for each feature in the dataframe
# and returns the name of the column with the greatest gain.

def select_attribute(features, classifications) :
    pass

# make_tree takes two required inputs
# 1. A dataframe consisting of the features to be considered
# 2. A Series containing the corresponding classifications.
# there are also two optional arguments:
# 1. zeror_val = the value generated by ZeroR
# 2 attr_dict  = a dictionary mapping variable names (such as outlook)
#   to a list of values (such as ['sunny','overcast','rainy']
# It's a recursive method.
# There are three base cases:
# 1. All the elements of classifications are the same.
#    We are at a leaf node. Create the node with this value as the classification
#    and return it.
# 2. There are no rows in the dataframe. In this case, we have no observations
#    for this set of feature values. So we are at a leaf. Create and return
#    a leaf node using ZeroR to set the value.
# 3. There are no columns in the dataframe. In this case, we had either
#    noise or missing observations preventing us from completely separating
#    the data. So we are at a leaf. Create and return
#    a leaf node using ZeroR to set the value.
# Then there is a recursive step:
#     use select_attribute to find the best attribute to split on.
#     construct a non-leaf node
#     For each value of that attribute, extract the rows that have that classification,
#     along with the corresponding classifications into a new dataframe and series.
#     Drop the column for this feature from these new Dataframes so we don't retest it.
#     Call make_tree with this new Dataframe and series and add the node that's
#     returned to the children, with key = feature name and value = Node.
#

def make_tree(features, classifications,zeror_val='play',attr_dict=None):
    pass


# classify takes two inputs:
# A node and a Series representing the data to classify.
# This is also a recursive function.
# Base case:
#   We are at a leaf. Return the value stored in classification.
# Recursive step:
#   Check what attribute node tests.
#   Get the value of data_to_classify for that feature.
#   Call classify on the child node corresponding to that value.




def classify(tree, data_to_classify) :
   pass

if __name__ == "__main__" :
    # set up for the tennis data
    attr_dict = {'outlook' : ['sunny','overcast','rainy'],
                 'temperature' : ['hot','mild','cool'],
                 'humidity' : ['high','normal'],
                 'windy' : ['weak','strong']}
    tennis_data = pd.read_csv('tennis.csv')
    features = tennis_data.iloc[:,:-1]
    classifications = tennis_data.iloc[:,-1]
    zeror_val = ZeroR(tennis_data)
    tree = make_tree(features, classifications, zeror_val, attr_dict)
    # we're using the training set to test. ick!
    for i in range (len(features)) :
        predicted_value = classify(tree, features.iloc[i])
        if predicted_value == classifications.iloc[i] :
            print("correct")
        else :
            print("incorrect")
