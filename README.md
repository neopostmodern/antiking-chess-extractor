# antiking-chess-extractor

## Usage

### Extraction

    usage: main.py [-h] [--offset number_of_plies] [--stride number_of_plies]
                   game_logs_directory

    Extract moves from game logs

    positional arguments:
      game_logs_directory   The folder containing the CSV game logs

    optional arguments:
      -h, --help            show this help message and exit
      --offset number_of_plies
                            Opening plies to skip
      --stride number_of_plies
                            Plies to skip after each selected move

### Permutation

    usage: permutate.py [-h] board_positions_file

    Permutate moves from FEN positions in file

    positional arguments:
      board_positions_file  The file containing the FEN notations

    optional arguments:
      -h, --help            show this help message and exit

## Usage example

    python3 main.py game-logs-server-2 --offset 5 --stride 2 --probability 0.8

For a complete run-trough see `execute.sh`

## Output

Is printed to `stdout`.
