import csv
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
parser.add_argument('start')
args = parser.parse_args()

start = int(args.start)


def clear():
    os.system('clear')


with open(args.input, 'r') as i_file:
    with open(args.output, 'a') as o_file:
        rd = csv.reader(i_file)
        wt = csv.writer(o_file)
        for i in range(start):
            rd = next(rd)
        for line in rd:
            s = line[1]
            print(s)
            label = int(input())
            if label != 0 and label != 1:
                print('wrong input')
                exit(-1)
            wt.writerow([label, s])
            clear()
