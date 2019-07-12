import csv
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('original')
parser.add_argument('noblank')
parser.add_argument('result')
args = parser.parse_args()

def restoreText(original):
    text = re.sub('[-=+,#/\?:^\n-❛˓◞˂̵✧$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', original)
    return text

with open(args.original, 'r') as i_file:
    with open(args.noblank, 'r') as i2_file:
        with open(args.result, 'w') as o_file:
            original = csv.reader(i_file)
            noblank = csv.reader(i2_file)
            original_line = []
            noblank_line = []
            label = []
            wt = csv.writer(o_file)
            i=0
            checker = False


            for line in original:
                original_line.append(line[1])

            for line in noblank:
                checker = False
                for line2 in original_line:
                    if line[1] == restoreText(line2) and checker == False:
                        i+=1
                        checker = True
                        wt.writerow([line[0], line2])