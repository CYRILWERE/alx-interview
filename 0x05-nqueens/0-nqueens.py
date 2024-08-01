#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_number_error_and_exit():
    print("N must be a number")
    sys.exit(1)

def print_size_error_and_exit():
    print("N must be at least 4")
    sys.exit(1)

def is_safe(board, row, col):
    """ Check if a queen can be placed on board at (row, col). """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    def backtrack(row, board):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0, board)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()
    
    if N < 4:
        print_size_error_and_exit()

    solutions = solve_nqueens(N)
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)

if __name__ == "__main__":
    main()

