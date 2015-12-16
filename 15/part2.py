#!/usr/bin/env python

import numpy as np


def score(amounts, specs):
    property_scores = amounts.dot(specs)
    property_scores[property_scores <= 0] = 0
    return np.prod(property_scores[0])


def calories(amounts, calorie_specs):
    return amounts.dot(calorie_specs.T)[0]


with open('input', 'r') as f:
    regex = r'.*: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
    all_specs = np.fromregex(f, regex, np.int)

property_specs = all_specs[:,:-1]
calorie_specs = all_specs[:,-1]
print property_specs
print calorie_specs

best_score = -1
for i in xrange(101):
    for j in xrange(101):
        for k in xrange(101):
            m = 100 - i - j - k

            amounts = np.array([[i, j, k, m]])

            if np.any(amounts < 0):
                continue

            if calories(amounts, calorie_specs) != 500:
                continue

            cur_score = score(amounts, property_specs)

            if cur_score > best_score:
                best_score = cur_score
                print amounts, best_score
