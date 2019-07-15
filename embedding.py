from Hangulpy import decompose, is_hangul
import csv
import argparse
import torch
import torch.nn as nn
import pickle


jamo_dictionary = dict()

def decompose_string(text):
    result = []
    for c in text:
        if is_hangul(c):
            result += [decompose(c)]
    return result


def add_to_dict(decomposed):
    for c in decomposed:
        for jamo in c:
            if jamo not in jamo_dictionary:
                jamo_dictionary[jamo] = 1+len(jamo_dictionary)


def to_index_array(decomposed, dict):
    result = []
    for c in decomposed:
        for jamo in c:
            result.append(dict[jamo])
    return result


def padding(arr, N):
    l = len(arr)
    if l > N:
        return arr[:N]
    else:
        for i in range(N-l):
            arr.append(0)
        return arr


def to_embedded_tensor(filename):
    strings = []
    labels = []
    with open(filename, 'r') as f:
        rdr = csv.reader(f)
        for line in rdr:
            s = line[1]
            decomposed = decompose_string(s)
            strings.append(decomposed)
            labels.append(int(line[0]))
            add_to_dict(decomposed)
    maxlen = 0
    for i in range(len(strings)):
        strings[i] = to_index_array(strings[i], jamo_dictionary)
        l = len(strings[i])
        maxlen = l if l > maxlen else maxlen

    # padding
    for i in range(len(strings)):
        strings[i] = padding(strings[i], maxlen)

    # strings = torch.LongTensor(strings)
    # labels = torch.FloatTensor(labels)
    #
    # embedding = nn.Embedding(len(jamo_dictionary)+1, dim)
    # # a = torch.LongTensor(1)
    # # print(embedding(a))
    #
    # embedded = []
    # for i in range(len(strings)):
    #     print('\rprocessing embedding %d/%d' % (i+1, len(strings)), end='')
    #     embedded.append(embedding(strings[i]).tolist())
    # embedded = torch.FloatTensor(embedded)
    # print('\nembedded tensor(shape): {}'.format(embedded.shape))

    with open('jamo.pydict', 'wb') as f:
        pickle.dump(jamo_dictionary, f)

    return strings, labels, (len(jamo_dictionary)+1)





