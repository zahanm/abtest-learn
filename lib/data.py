
from datetime import datetime, timedelta
import os.path
from random import randint, choice
import sqlite3

import names

NUM_PEOPLE = 100
NUMBER_OF_HITS = 20
DATA_DIR = '../data'
DB_FILE = 'site.db'

def run():
  conn = sqlite3.connect(os.path.join(DATA_DIR, DB_FILE))
  # p = People(conn)
  # p.filltable()
  s = Simulator(conn)
  for i in range(NUMBER_OF_HITS):
    s.serverhit()
  s.flushlogs()

class Simulator:
  """
  Simulates a webservice receiving requests and logging each one
  """

  def __init__(self, db):
    # initialize this service 5 days ago
    self.current_time = datetime.now() - timedelta(days=5)
    self.db = db
    with self.db:
      self.db.execute('drop table logs')
      self.db.execute('create table logs (ts timestamp, uid integer, name text)')
      self.people = list(self.db.execute('select uid, name from people'))
    assert NUM_PEOPLE == len(self.people)
    self.transactions = []

  def serverhit(self):
    secs_elapsed = randint(0, 10)
    self.current_time += timedelta(seconds=secs_elapsed)
    person = choice(self.people)
    uid = person[0]
    name = person[1]
    self.transactions.append((self.current_time, uid, name))

  def flushlogs(self):
    with self.db:
      self.db.executemany('insert into logs values (?,?,?)', self.transactions)

class People:

  def __init__(self, db):
    self.db = db
    with self.db:
      self.db.execute('create table people (uid integer primary key, name text)')

  def filltable(self):
    peeps = map(
      lambda ii: (ii, names.makeupone()),
      range(1, NUM_PEOPLE + 1)
    )
    with self.db:
      self.db.executemany('insert into people values (?, ?)', peeps)

if __name__ == '__main__':
  run()
