#!/usr/bin/env python
"""Solve AoC 2015 Day 18, Part 1"""


def count_neighbors(grid, i, j):
    """Count lit eight-connected neighbors.

    Calculate all neighbors and check if they're already on
    (i.e., in the grid)
    """
    return sum(((x, y) in grid
                for x in (i - 1, i, i + 1)
                for y in (j - 1, j, j + 1)
                if (x, y) != (i, j)))


def evolve(grid):
    """Perform one game-of-life step."""
    next_grid = set()

    for i in xrange(100):
        for j in xrange(100):
            n = count_neighbors(grid, i, j)

            if (i, j) in grid and 2 <= n <= 3:
                next_grid.add((i, j))

            if (i, j) not in grid and n == 3:
                next_grid.add((i, j))

    return next_grid

num_steps = 100


def main():
    """Entry point"""

    with open('input', 'r') as f:
        # Create a tuple for all the lit lights, and collect them
        grid = {(x, y) for y, line in enumerate(f)
                for x, char in enumerate(line.strip())
                if char == '#'}

    for _ in xrange(num_steps):
        grid = evolve(grid)

    lights_on = len(grid)

    print 'There are {} lights left on'.format(lights_on)

if __name__ == "__main__":
    main()
