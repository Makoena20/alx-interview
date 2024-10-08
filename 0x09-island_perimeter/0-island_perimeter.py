#!/usr/bin/python3
"""
Module to calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    The island is represented by 1's and water by 0's.

    Args:
        grid (list): A list of lists of integers representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract edges that are shared with another land cell
                if i > 0 and grid[i - 1][j] == 1:  # Cell above is land
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Cell to the left is land
                    perimeter -= 2

    return perimeter

