from typing import List
import time

class game_of_life:
    def gameOfLife(self, board: List[List[int]]) -> List[List[int]]:
        """
        Modify the board in-place and return the updated board.
        """

        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                elif copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
        
        return board  # Return the modified board


# Function to print the board
def print_board(board):
    for row in board:
        print(row)
    print()


# Example usage:
if __name__ == "__main__":
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    # Create an instance of the game_of_life class
    game = game_of_life()

    # Run the game for multiple iterations (generations)
    generations = 5  # Set how many generations you want to simulate

    for gen in range(generations):
        print(f"Generation {gen + 1}:")
        print_board(board)  # Print the current board
        board = game.gameOfLife(board)  # Update the board
        time.sleep(1)  # Optional: add delay to simulate the game evolving slowly
