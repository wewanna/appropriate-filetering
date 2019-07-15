import csv
import random

input = 'labeled_data.csv'
output = 'labeled_data_reduced.csv'

with open(input, 'r') as f:
    rdr = csv.reader(f)
    normal = []
    yok = []
    for line in rdr:
        label = int(line[0])
        if 0 == label:
            normal.append(line[1])
        else:
            yok.append(line[1])
    print('normal:{}, yok:{}'.format(len(normal), len(yok)))

    random.shuffle(normal)
    with open(output, 'w') as outf:
        wrt = csv.writer(outf)
        for i in range(len(yok)):
            wrt.writerow([0, normal[i]])
            wrt.writerow([1, normal[i]])



