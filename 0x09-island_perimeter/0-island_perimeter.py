#!/usr/bin/python3
"""
0-island_perimeter
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    :param grid: List of list of integers where 0 represents water and 1 represents land
    :return: The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the upper cell
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the lower cell
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left cell
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right cell
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter

