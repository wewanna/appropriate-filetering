from Hangulpy import decompose, is_hangul
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
# parser.add_argument('output')
parser.add_argument('D')
args = parser.parse_args()

dimension = int(args.D)
print('dimension: {}'.format(dimension))

jamo_dictionary = dict()

def decompose_string(text):
    result = []
    for c in text:
        if is_hangul(c):
            result += [decompose(c)]
    return result


def add_to_dict(composed):
    for c in composed:
        for jamo in c:
            if jamo not in jamo_dictionary:
                jamo_dictionary[jamo] = len(jamo_dictionary)


with open(args.input, 'r') as f:
    rdr = csv.reader(f)
    for line in rdr:
        s = line[1]
        add_to_dict(decompose_string(s))

print(len(jamo_dictionary))
print(jamo_dictionary)





