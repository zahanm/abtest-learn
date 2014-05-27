
import os.path
import sqlite3

DATA_DIR = '../data'
DB_FILE = 'site.db'

class Analysis:
  """
  Helper to parse out the data from the sqlite database
  """
  def __init__(self):
    self.db = sqlite3.connect(os.path.join(DATA_DIR, DB_FILE))

  def countexposures(self):
    with self.db:
      res = self.db.execute('select count(*) from exposures').fetchone()
      return res[0]

  def countconversions(self):
    with self.db:
      res = self.db.execute('select count(*) from conversions').fetchone()
      return res[0]

if __name__ == '__main__':
  print('This file is not meant to be run directly.')
