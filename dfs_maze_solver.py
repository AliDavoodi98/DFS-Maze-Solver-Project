# -*- coding: utf-8 -*-
"""Untitled91.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dQ2_gVP8Uwo1D0uEEE_bbC9fkDxijLXK
"""

import argparse
import matplotlib.pyplot as plt
import numpy as np
import ast


class DFS_PATH:
    def __init__(self, matrix):
        self.cache = {}
        self.matrix = np.array(matrix)  # Convert matrix to a numpy array
        self.neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.rows, self.cols = self.matrix.shape
        self.fig, self.ax = plt.subplots()  # Prepare a matplotlib figure

    def draw_matrix(self, current_row=None, current_column=None):
        self.ax.clear()  # Clear previous state
        self.ax.matshow(self.matrix, cmap='viridis')

        if current_row is not None and current_column is not None:
            self.ax.text(current_column, current_row, 'Current', color='red', ha='center', va='center')

        for i in range(self.rows + 1):
            self.ax.axhline(i - 0.5, color='k', linewidth=1)
        for j in range(self.cols + 1):
            self.ax.axvline(j - 0.5, color='k', linewidth=1)

        plt.pause(0.5)  # Pause to visualize the update

    def path_finder(self):
        max_path_length = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i, j] == 1:
                    self.draw_matrix(i, j)
                    max_path_length = max(max_path_length, self.recurse_path(i, j))
        plt.show()  # Show the final state
        return max_path_length

    def recurse_path(self, current_row, current_column):
        if current_row < 0 or current_column < 0 or current_row >= self.rows or current_column >= self.cols or self.matrix[current_row, current_column] == 0:
            return 0

        if (current_row, current_column) in self.cache:
            return self.cache[(current_row, current_column)]

        original_value = self.matrix[current_row, current_column]
        self.matrix[current_row, current_column] = 0
        self.draw_matrix(current_row, current_column)

        max_length = 1
        for di, dj in self.neighbor_offsets:
            ni, nj = current_row + di, current_column + dj
            length = self.recurse_path(ni, nj)
            max_length = max(max_length, 1 + length)

        self.matrix[current_row, current_column] = original_value
        self.cache[(current_row, current_column)] = max_length
        return max_length

def main(matrix_string):
    # Convert string representation of matrix to list of lists
    try:
        matrix = ast.literal_eval(matrix_string)
        if not all(isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("Invalid matrix format")
    except (SyntaxError, ValueError) as e:
        print(f"Error parsing matrix: {e}")
        return

    dfs_path = DFS_PATH(matrix)
    result = dfs_path.path_finder()
    print(f"Maximum Path Length: {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DFS Path Visualization.')
    parser.add_argument('--matrix', type=str, required=True, help='Matrix as a string')
    args = parser.parse_args()

    main(args.matrix)
