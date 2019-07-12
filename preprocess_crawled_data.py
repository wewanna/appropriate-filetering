import csv
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

def cleanText(original):
    text = re.sub('[-=+,#/\?:^-❛˓◞\n\r˂̵✧$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', original)
    return text

with open(args.input, 'r') as i_file:
    with open(args.output, 'w') as o_file:
        rd = csv.reader(i_file)
        wt = csv.writer(o_file)
        for line in rd:
            s = line[1]
            ln = len(s)
            if ln < 2:
                continue
            last = s[ln-8:]
            if last == '- dc App':
                s = s[:ln-8]
            s = cleanText(s)
            wt.writerow([line[0], s])


