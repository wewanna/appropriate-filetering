import csv
import os
import argparse
from itertools import islice

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
parser.add_argument('start')
args = parser.parse_args()

start = int(args.start)
if start < 1:
    print('start should be greater than 0')
    exit(-1)


def clear():
    os.system('clear')


count = start
with open(args.input, 'r') as i_file:
    with open(args.output, 'a') as o_file:
        rd = csv.reader(i_file)
        wt = csv.writer(o_file)
        for line in islice(rd, start-1, None):
            s = line[1]
            print(s)
            label = input()
            if label == 'q':
                break
            count += 1
            if label == '2':
                continue
            label = int(label)
            if label != 0 and label != 1:
                print('wrong input')
                exit(-1)
            wt.writerow([label, s])
            clear()
        wt.writerow(['next', count])
