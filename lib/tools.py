
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

  def raw_names_ages_gender(self, limit: int):
    with self.db:
      res = self.db.execute(
        'select name, age, gender from people limit ?',
        (limit, ),
      )
      return list(res)

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

  def raw_metrics_for_test(self, test1: bool, test2: bool):
    with self.db:
      res = self.db.execute(
        '''
        select c.metric
        from conversions as c
        join exposures as e
        on c.uid = e.uid
        where e.test1 = ? and e.test2 = ?
        ''',
        (int(test1), int(test2)),
      )
      return np.array(
        [ord(r[0]) - ord('A') for r in res],
        np.int,
      )

  def raw_ages_for_test_metric(self, test1: bool, test2: bool, metric: str):
    with self.db:
      res = self.db.execute(
        '''
        select p.age
        from people as p
        join exposures as e
        on p.uid = e.uid
        join conversions as c
        on c.uid = p.uid
        where e.test1 = ? and e.test2 = ? and c.metric = ?
        ''',
        (int(test1), int(test2), metric),
      )
      return np.array(list(res), np.int)

  def raw_genders_for_test_metric(self, test1: bool, test2: bool, metric: str):
    with self.db:
      res = self.db.execute(
        '''
        select p.gender
        from people as p
        join exposures as e
        on p.uid = e.uid
        join conversions as c
        on c.uid = p.uid
        where e.test1 = ? and e.test2 = ? and c.metric = ?
        ''',
        (int(test1), int(test2), metric),
      )
      return np.array(
        [r[0] == 'm' for r in res],
        np.bool,
      )

  def uid_counts_for_test_metric(self, test1: bool, test2: bool, metric: str):
    with self.db:
      res = self.db.execute(
        '''
        select c.uid, count(*)
        from conversions as c
        join exposures as e
        on c.uid = e.uid
        where e.test1 = ? and e.test2 = ? and c.metric = ?
        group by c.uid
        ''',
        (int(test1), int(test2), metric),
      )
      return np.array(list(res), np.int)

if __name__ == '__main__':
  print('This file is not meant to be run directly.')
