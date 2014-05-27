
from datetime import datetime, timedelta
import os.path
from random import randint, choice, random
import sqlite3

import names

NUM_PEOPLE = 100
YOUNGEST_AGE = 10
MID_LIFE = 20
OLDEST_AGE = 30
NUMBER_OF_HITS = 1000
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

  def __init__(self, db: sqlite3.Connection):
    # initialize this service 5 days ago
    self.current_time = datetime.now() - timedelta(days=5)
    self.db = db
    # format: (uid, age, gender)
    self.people = []
    with self.db:
      self.db.execute('drop table if exists exposures')
      self.db.execute('create table exposures (ts timestamp, uid integer unique, test1 integer, test2 integer)')
      self.db.execute('drop table if exists conversions')
      self.db.execute('create table conversions (ts timestamp, uid integer, conversion text)')
      self.people = list(self.db.execute('select uid, age, gender from people'))
    assert NUM_PEOPLE == len(self.people)
    self.exposures = []
    self.conversions = []

  def serverhit(self):
    secs_elapsed = randint(0, 10)
    self.current_time += timedelta(seconds=secs_elapsed)
    person = choice(self.people)
    uid = person[0]
    age = person[1]
    gender = person[2]
    test1, test2 = self.expose(uid)
    convs = self.convert(test1, test2, age, gender)
    self.exposures.append((self.current_time, uid, int(test1), int(test2)))
    for conv in convs:
      self.conversions.append((self.current_time, uid, conv))

  def expose(self, uid: int) -> (bool, bool):
    # usually we'd calculate a hash ID for the group mapping, but in this toy example, UID - 1 gives a number in [0, 99)
    hash_key = uid - 1
    test1 = hash_key < 20
    test2 = 10 <= hash_key and hash_key < 30
    return test1, test2

  def convert(self, test1: bool, test2: bool, age: int, gender: str):
    convs = []
    if self.convert_a(test1, test2, age, gender):
      convs.append('A')
    if self.convert_b(test1, test2, age, gender):
      convs.append('B')
    if self.convert_c(test1, test2, age, gender):
      convs.append('C')
    return convs

  def convert_a(self, test1: bool, test2: bool, age: int, gender: str):
    pA = 0.3
    testdelta = 0
    if test2:
      testdelta = 0.02 * pA
    pA += testdelta
    return random() < pA

  def convert_b(self, test1: bool, test2: bool, age: int, gender: str):
    testdelta = 0
    if age < MID_LIFE:
      if gender == 'm':
        pB = 0.2
      else:
        pB = 0.15
    else:
      if gender == 'm':
        pB = 0.1
      else:
        pB = 0.05
    if test1:
      testdelta = 0.1 * pB
    pB += testdelta
    return random() < pB

  def convert_c(self, test1: bool, test2: bool, age: int, gender: str):
    pC = 0.05
    testdelta = 0
    if test1:
      if gender == 'm':
        testdelta = 0.02 * pC
      else:
        testdelta = -0.01 * pC
    if test2:
      testdelta = -0.02 * pC
    pC += testdelta
    return random() < pC

  def flushlogs(self):
    with self.db:
      # ignores when there is a row with that UID already present
      self.db.executemany('insert or ignore into exposures values (?, ?, ?, ?)', self.exposures)
      self.db.executemany('insert into conversions values (?, ?, ?)', self.conversions)

class People:

  def __init__(self, db: sqlite3.Connection):
    self.db = db
    with self.db:
      self.db.execute('drop table if exists people')
      self.db.execute('create table people (uid integer primary key, name text, age integer, gender text)')

  def filltable(self):
    def makeperson(ii):
      age = randint(YOUNGEST_AGE, OLDEST_AGE)
      gender = choice(['m', 'f'])
      name = names.makeupone(gender)
      return (ii, name, age, gender)
    peeps = map(
      makeperson,
      range(1, NUM_PEOPLE + 1)
    )
    with self.db:
      self.db.executemany('insert into people values (?, ?, ?, ?)', peeps)

if __name__ == '__main__':
  run()
