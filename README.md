# Tic Tac Toe Game with AI

This is a console-based Tic Tac Toe game implemented in Python. The game features an AI opponent that uses the minimax algorithm to make optimal moves.

## Features

- **Human vs AI**: Play against an AI opponent.
- **Minimax Algorithm**: The AI uses the minimax algorithm to make decisions, ensuring it plays optimally.
- **Console-based**: Simple text-based interface to play the game in the terminal.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    git clone https://github.com/yourusername/tic-tac-toe-ai.git
    cd tic-tac-toe-ai
    

2. (Optional) Create a virtual environment:
    python -m venv venv
    source venv/bin/activate 

### Running the Game

To start the game, run the following command:
python tic_tac_toe.py
How to Play
The game board is displayed with empty spaces.
Human player ('O') starts first.
Enter your move by specifying the row and column numbers (0, 1, or 2).
The AI ('X') will then make its move.
Continue until there is a winner or the board is full (resulting in a draw).
Example Gameplay

 |   |  
-----
 |   |  
-----
 |   |  
Enter your move (row and column): 0 0
O |   |  
-----
 |   |  
-----
 |   |  
AI's turn...
O |   |  
-----
 | X |  
-----
 |   |  
Enter your move (row and column): 1 1
O |   |  
-----
 | O |  
-----
 |   |  
AI's turn...
O |   |  
-----
 | O | X
-----
 |   |  
...

Game Over
The game ends when either player wins or the board is full. The result will be displayed in the console.

Implementation Details
The AI uses the minimax algorithm to determine the optimal move. Here's a brief explanation of the functions used:

print_board(board): Prints the current state of the board.
check_winner(board): Checks if there is a winner.
is_full(board): Checks if the board is full.
minimax(board, depth, is_maximizing): Implements the minimax algorithm to evaluate the game state.
find_best_move(board): Finds the best move for the AI player.
Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
