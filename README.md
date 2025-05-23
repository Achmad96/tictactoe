# Tictactoe

## Installation

### Prerequisites

- Python 3.x installed on your system

### Steps to Install

1. Clone or download this repository to your local machine
2. Navigate to the tictactoe directory:
   ```
   cd path/to/tictactoe
   ```
3. No additional dependencies are required!

## How to Play

### Starting the Game

Run the game with:

```
python tictactoe.py
```

### Game Rules

- Tictactoe (also known as Tic-Tac-Toe or Noughts and Crosses) is a game for two players
- The game is played on a 3×3 grid
- Player 1 uses 'X' and Player 2 uses 'O'
- Players take turns placing their mark in an empty cell
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins
- If all cells are filled and no player has won, the game is a draw

### Controls

- When prompted, enter a number from 1-9 to place your mark on the grid
- The grid positions correspond to these numbers:
  ```
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
  ```

### Example

When it's your turn, you'll see a prompt like:

```
Player-1:
Player-2:
```

Enter a number and press Enter to make your move.

## Troubleshooting

- If you choose a position that's already taken, you'll receive a message and need to try again
- Invalid inputs (non-numbers or numbers outside 1-9) will be ignored
