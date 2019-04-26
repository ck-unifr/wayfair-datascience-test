# Problem:
# You can solve the following problem in either Python or R.
# You are given a dictionary/list representing a basket with different types of fruits in it.
# The keys describe the type of fruit,the values their quantity.
# For example, your dictionary/list might look like the following:
# Python version: fruit_basket = {‘apple’: 7, ‘banana’: 3, ‘orange’: 5}
# R version: fruit_basket = list(apple = 7, banana = 3, orange = 5)
#
# Write a function that takes this dictionary/list as input and returns a fruit picked from the
# basket according to the likelihood of picking each fruit:
# - The function should be called pick_fruit
# - It should return the label of the fruit, e.g. in this example “apple”, “banana”, or “orange”
# - It should generalize to arbitrary fruit baskets, i.e. baskets containing fruits and quantities that are different from the example above
# - It should run efficiently for very large numbers of types and quantities of fruits
#
#
#
# author: Kai Chen
# date: April, 2019
#

import random
import numpy as np

def pick_fruit(fruit_basket):
    """
    The function takes a dictionary/list as input and returns a fruit picked from the basket according to the likelihood of picking each fruit.
    :param a dictionary, keys describe the type of fruit,the values their quantity. For example: fruit_basket = {‘apple’: 7, ‘banana’: 3, ‘orange’: 5}
    :return: a string presents the fruit picked from the basket according to the likelihood of picking each fruit.
    """
    fruit = ''

    # compute the sum of the fruit
    fruit_sum = sum(fruit_basket.values())

    fruit_list = list(fruit_basket.keys())

    # compute the probabilities
    fruit_prob = dict()
    if fruit_sum == 0:
        for key, value in fruit_basket.items():
            fruit_prob[key] = 0
    else:
        for key, value in fruit_basket.items():
            fruit_prob[key] = value*1.0/fruit_sum

    #print(fruit_prob.keys())
    #print(fruit_prob.values())

    fruit_index = np.random.choice(len(fruit_prob.keys()), 1, p=list(fruit_prob.values()))

    fruit = list(fruit_prob.keys())[fruit_index[0]]

    return fruit

if __name__ == '__main__':
    fruit_basket = {'apple': 7, 'banana': 3, 'orange': 5}

    for i in range(10):
        fruit_picked = pick_fruit(fruit_basket)
        print(fruit_picked)