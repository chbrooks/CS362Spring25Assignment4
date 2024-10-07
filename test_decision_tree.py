from unittest import TestCase
from decision_tree import *

class Test(TestCase):
    def test_entropy(self):
        data = pd.Series(['no', 'no', 'yes', 'yes', 'yes', 'no',
                          'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no'])
        e = entropy(data)
        self.assertAlmostEqual(e, 0.94, places=2)

    def test_gain(self):
        tennis_variables = pd.Series(['sunny', 'sunny', 'sunny', 'sunny', 'sunny',
                            'overcast', 'overcast', 'overcast', 'overcast',
                            'rainy', 'rainy', 'rainy', 'rainy', 'rainy'])
        tennis_classes = pd.Series(['yes', 'yes', 'no', 'no', 'no',
                          'yes', 'yes', 'yes', 'yes',
                          'yes', 'yes', 'yes', 'no', 'no'])

        test_variables = pd.Series([1, 2, 1, 2, 1, 2, 1, 2])
        test_classes1 = pd.Series([0, 1, 0, 1, 0, 1, 0, 1])
        ## gain should be 1
        print(gain(test_variables, test_classes1))
        test_classes2 = pd.Series([0, 0, 0, 0, 1, 1, 1, 1])
        ## gain should be 0
        print(gain(test_variables, test_classes2))
        ## gain should be 0.25
        print(gain(tennis_variables, tennis_classes))
        data = pd.read_csv('tennis.csv')
        indep_vars = data['outlook']
        dep_vars = data['play']
        print(gain(indep_vars, dep_vars))

    def test_select_attribute(self):
        self.fail()

    def test_make_tree(self):
        self.fail()

    def test_classify(self):
        self.fail()


