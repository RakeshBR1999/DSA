def tictactoe(moves):
    board = [["" for _ in range(3)] for _ in range(3)]

    # Fill the board
    for i, (row, col) in enumerate(moves):
        player = "A" if i % 2 == 0 else "B"
        board[row][col] = "X" if player == "A" else "O"
        print(board)
    # Function to check winner
    def check_winner(symbol):
        # Check rows and columns
        for i in range(3):
            if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
                return True
        # Check diagonals
        # what all does is check if all the elements in the diagonal are equal to the symbol
        if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    # Check for winner
    if check_winner("X"):
        return "A"
    if check_winner("O"):
        return "B"

    # Check for draw or pending
    return "Draw" if len(moves) == 9 else "Pending"

# Time Complexity: O(1) — The board size is fixed (3x3), so the operations are constant time.
# Space Complexity: O(1) — The board size is fixed (3x3), so the space used is constant.

# Example usage:
# moves = [[0, 0], [1, 1], [0, 1], [1, 0], [0, 2]]
# print(tictactoe(moves))  # Output: "A" (Player A wins)
# Example usage:
# moves = [[0, 0], [1, 1], [0, 1], [1, 0], [2, 2]]
# print(tictactoe(moves))  # Output: "A" (Player A wins)
# # Example usage:
# moves = [[0, 0], [1, 1], [0, 1], [1, 0], [2, 2], [2, 1], [2, 0]]
# print(tictactoe(moves))  # Output: "B" (Player B wins)
# # Example usage:
moves = [[0, 0], [1, 1], [0, 1], [1, 0], [2, 2], [2, 1], [2, 0], [1, 2]]
print(tictactoe(moves))  # Output: "Draw" (Game is a draw)