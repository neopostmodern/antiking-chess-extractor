#!/usr/bin/env bash

python3 main.py game-logs-server-2 > board-positions.txt
python3 main.py game-logs-server-3 >> board-positions.txt
sort board-positions.txt | uniq > board-positions-unique.txt

python3 permutate.py board-positions-unique.txt > board-permutations.txt
sort board-permutations.txt | uniq > board-permutations-unique.txt

# print results:
# wc -l < board-permutations-unique.txt