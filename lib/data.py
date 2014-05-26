
from datetime import datetime, timedelta
import os.path
from random import randint
import sqlite3

import names

NUMBER_OF_HITS = 20
DATA_DIR = '../data'
DB_FILE = 'site.db'

def run():
  conn = sqlite3.connect(os.path.join(DATA_DIR, DB_FILE))
  s = Simulator(conn)
  for i in range(NUMBER_OF_HITS):
    s.serverhit()

class Simulator:
  """
  Simulates a webservice receiving requests and logging each one
  """

  def __init__(self, db):
    # initialize this service 5 days ago
    self.current_time = datetime.now() - timedelta(days=5)
    self.db = db
    with self.db:
      self.db.execute('create table logs (ts timestamp, uid integer, name text)')

  def serverhit(self):
    secs_elapsed = randint(0, 10)
    self.current_time += timedelta(seconds=secs_elapsed)
    uid = 0
    name = names.makeupone()
    with self.db:
      self.db.execute('insert into logs values (?,?,?)', (self.current_time, uid, name))

if __name__ == '__main__':
  run()
