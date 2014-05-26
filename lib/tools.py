
import os.path
import sqlite3

DATA_DIR = '../data'
DB_FILE = 'site.db'

def countlines():
  conn = sqlite3.connect(os.path.join(DATA_DIR, DB_FILE))
  with conn:
    for res in conn.execute('select count(*) from logs'):
      print('{} rows in file'.format(res[0]))

if __name__ == '__main__':
  countlines()
