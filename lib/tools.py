
import csv
import os.path

DATA_DIR = '../data'

def countlines():
  with open(os.path.join(DATA_DIR, 'logs.csv'), newline='') as f:
    num_rows = 0
    for row in csv.DictReader(f):
      num_rows += 1
    print('{} rows in file'.format(num_rows))

if __name__ == '__main__':
  countlines()
