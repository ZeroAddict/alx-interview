#!/usr/bin/python3

"""Solution to the N-Queens Problem"""

import sys

def explore_solutions(row, num_queens, occupied_columns, positive_diagonals, negative_diagonals, chessboard):
    """
    Recursive function to find all solutions.
    
    Args:
        row (int): Current row index.
        num_queens (int): Total number of queens.
        occupied_columns (set): Columns already occupied.
        positive_diagonals (set): Positive diagonals occupied.
        negative_diagonals (set): Negative diagonals occupied.
        chessboard (list): Current state of the board.
    """
    
    if row == num_queens:
        # Found a solution, print queen positions
        solution = []
        for i in range(len(chessboard)):
            for j in range(len(chessboard[i])):
                if chessboard[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    
    for col in range(num_queens):
        if col in occupied_columns or (row + col) in positive_diagonals or (row - col) in negative_diagonals:
            # Skip occupied columns and diagonals
            continue
        
        occupied_columns.add(col)
        positive_diagonals.add(row + col)
        negative_diagonals.add(row - col)
        chessboard[row][col] = 1
        
        explore_solutions(row + 1, num_queens, occupied_columns, positive_diagonals, negative_diagonals, chessboard)
        
        occupied_columns.remove(col)
        positive_diagonals.remove(row + col)
        negative_diagonals.remove(row - col)
        chessboard[row][col] = 0

def solve_n_queens(num_queens):
    """
    Finds all solutions to the N-Queens problem.
    
    Args:
        num_queens (int): Number of queens.
    
    Returns:
        None
    """
    
    occupied_columns = set()
    positive_diagonals = set()
    negative_diagonals = set()
    chessboard = [[0] * num_queens for _ in range(num_queens)]
    
    explore_solutions(0, num_queens, occupied_columns, positive_diagonals, negative_diagonals, chessboard)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        num_queens = int(sys.argv[1])
        if num_queens < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_n_queens(num_queens)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
