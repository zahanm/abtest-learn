
import numpy as np
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

  def count_exposures(self):
    with self.db:
      res = self.db.execute('select count(*) from exposures').fetchone()
      return res[0]

  def count_conversions(self):
    with self.db:
      res = self.db.execute('select count(*) from conversions').fetchone()
      return res[0]

  def raw_ages(self):
    with self.db:
      res = self.db.execute('select age from people')
      return np.array(list(res), np.int)

  def raw_genders(self):
    with self.db:
      return np.array(
        [res[0] == 'm' for res in self.db.execute('select gender from people')],
        np.bool,
      )

  def raw_uids_from_exposures(self):
    with self.db:
      res = self.db.execute('select uid from exposures')
      return np.array(list(res), np.int)

  def uids_with_counts_from_conversions(self):
    with self.db:
      res = self.db.execute('select uid, count(*) from conversions group by uid')
      return np.array(list(res), np.int)

if __name__ == '__main__':
  print('This file is not meant to be run directly.')
