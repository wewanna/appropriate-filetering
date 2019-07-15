from selenium import webdriver
import argparse
import csv
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('N')
parser.add_argument('startpage')
parser.add_argument('output')
args = parser.parse_args()

N = int(args.N)
start = int(args.startpage)
output_filename = args.output

print('N = %d, start=%d, output=%s'%(N, start, output_filename))

driver = webdriver.Chrome('./chromedriver')
base_url = 'https://gall.dcinside.com/board/view/?id=game1_new&no='

output_file = open(output_filename, 'w')
wr = csv.writer(output_file)

def read(url):
    driver.get(url)
    print('get %s' % url)
    comments = driver.find_elements_by_css_selector('p.usertxt.ub-word')
    count = 0
    for comment in comments:
        value = comment.text
        print(value)
        wr.writerow([0, value])
        count += 1
        if count > 7000:
            break

for i in range(N):
    read(base_url+str(start-i))
    sleep(2)

output_file.close()
