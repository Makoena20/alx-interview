# Prime Game

This project implements a game played between two players, Maria and Ben, using prime numbers. The players take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including `n`. The player who cannot make a move loses the game.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style compliance

## Usage

The main function to determine the winner is `isWinner(x, nums)`, where:

- `x` is the number of rounds.
- `nums` is an array of integers representing the upper limit of the sets for each round.

### Example

```python
result = isWinner(3, [4, 5, 1])
print("Winner:", result)

