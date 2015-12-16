#!/usr/bin/env python

import numpy as np

def score(amounts, specs):
    property_scores = amounts.dot(specs)
    property_scores[property_scores <= 0] = 0
    return np.prod(property_scores[0])

def best_improvement(amounts, specs):
    cur_score = score(amounts, specs)
    best_score = cur_score
    best_amounts = amounts

    # For every ingredient
    for i in xrange(len(amounts[0])):
        # For both directions
        for direction in [-1, 1]:
            # For every other ingredient
            for j in xrange(i, len(amounts[0])):
                if i == j:
                    continue

                new_amounts = np.copy(amounts)
                new_amounts[0, i] += direction
                new_amounts[0, j] -= direction

                if np.any(new_amounts < 0):
                    continue

                new_score = score(new_amounts, specs)

                if new_score > best_score:
                    best_score = new_score
                    best_amounts = new_amounts

    return (best_amounts, best_score - cur_score)


with open('input', 'r') as f:
    regex = r'.*: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+)'
    specs = np.fromregex(f, regex, np.int)

# Start with a decent guess
num_ingredients = len(specs)
total_capacity = 100

start_amount = total_capacity / num_ingredients
amounts = np.ones((1, num_ingredients), np.int) * start_amount
# Correct for the slack
amounts[0, -1] = total_capacity - (start_amount * (num_ingredients - 1))

initial_score = score(amounts, specs)

# Find the best dimensional improvement
(new_amounts, new_score) = best_improvement(amounts, specs)
while new_score > 0:
    (new_amounts, new_score) = best_improvement(new_amounts, specs)
    print new_amounts, new_score

print 'Best amounts got score {}'.format(score(new_amounts, specs))
print '  {}'.format(new_amounts)
