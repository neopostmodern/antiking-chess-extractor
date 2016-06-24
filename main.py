import csv
import argparse
import os
import glob
from random import random

parser = argparse.ArgumentParser(description='Extract moves from game logs')
parser.add_argument('directory', metavar='game_logs_directory', type=str, help='The folder containing the CSV game logs')
parser.add_argument('--offset', metavar='number_of_plies', dest='offset', action='store', default=0, type=int, help='Opening plies to skip')
parser.add_argument('--stride', metavar='number_of_plies', dest='stride', action='store', default=1, type=int, help='Plies to skip after each selected move')
parser.add_argument('--probability', metavar='bernoulli', dest='probability', action='store', default=1, type=float, help='Probability of selecting a move')

args = parser.parse_args()

if not os.path.isdir(args.directory):
    print("Not a directory (or does not exist: %s" % args.directory)
    exit(1)

for game_log_file_name in glob.glob(os.path.join(args.directory, '*.csv')):
    remaining_offset = args.offset
    remaining_stride = 0

    with open(game_log_file_name, newline='') as game_log_file:
        csv_reader = csv.reader(game_log_file, delimiter=';')

        header = True
        block_index = 0
        for row_index, row in enumerate(csv_reader):
            if header:
                header = False
                continue

            if len(row) == 0:
                block_index += 1
                header = True
                continue

            # game & player info
            if block_index == 1:
                continue

            # actual game
            elif block_index == 2:
                if row[0] == 'end':
                    break
                    # results unnecessary

                if remaining_offset > 0:
                    remaining_offset -= 1
                    continue

                if remaining_stride > 1:
                    remaining_stride -= 1
                    continue

                if random() > args.probability:
                    continue

                print(row[4])
                remaining_stride = args.stride




