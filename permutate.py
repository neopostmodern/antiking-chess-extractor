import csv
import argparse
import os
import glob


parser = argparse.ArgumentParser(description='Permutate moves from FEN positions in file')
parser.add_argument('file', metavar='board_positions_file', type=str, help='The file containing the FEN notations')

args = parser.parse_args()

if not os.path.isfile(args.file):
    print("Not a file (or does not exist: %s)" % args.file)
    exit(1)

with open(args.file, newline='') as fen_file:
    for line in fen_file:
        line = line.rstrip()
        # print("> %s" % line)

        for position, character in enumerate(line):
            if character == ' ':
                break
            if character in 'aAkK':  # is a type of king
                continue
            if character == '/':  # separator
                continue
            if character.isdigit():  # fen 'whitespace'
                continue

            white_space_before = 0
            new_fen = ''

            if position > 0 and line[position - 1].isdigit():
                white_space_before = int(line[position - 1])
                new_fen = line[:position - 1]
            else:
                new_fen = line[:position]

            if line[position + 1].isdigit():
                white_space_after = int(line[position + 1])
                new_fen += "%d%s" % (white_space_before + white_space_after + 1, line[position + 2:])
            else:
                new_fen += "%d%s" % (white_space_before + 1, line[position + 1:])

            # print("%d %s : %s" % (position, character, new_fen))
            print(new_fen)
