# Island Perimeter Project

## Overview
This project involves calculating the perimeter of an island represented within a grid. The grid is a 2D list of integers where `0` represents water and `1` represents land. The goal is to implement a function that returns the perimeter of the island based on the grid configuration.

## Requirements
- Python 3.4.3 or later
- The script must be executable and adhere to PEP 8 style guidelines (version 1.7).
- The function should not import any external modules.

## Files
- `0-island_perimeter.py`: Contains the implementation of the `island_perimeter` function.
- `0-main.py`: A script to test the `island_perimeter` function with a sample grid.
- `README.md`: This file, providing an overview and instructions.

## Function Description
### island_perimeter(grid)
- **Parameters**: 
  - `grid`: A list of lists of integers where `0` represents water and `1` represents land.
- **Returns**: 
  - An integer representing the perimeter of the island.
- **Description**: 
  - The function iterates through each cell in the grid. For every land cell (`1`), it checks its neighbors (up, down, left, and right). If a neighbor is water (`0`) or out of bounds (indicating the edge of the grid), it contributes to the perimeter.

## Example
Here is an example to illustrate how the function works:

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Expected output: 12

