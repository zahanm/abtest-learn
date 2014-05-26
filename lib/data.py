
import csv
from datetime import datetime, timedelta
import os.path
from random import randint

DATA_DIR = '../data'
FIELDNAMES = [
  'timestamp',
  'uid',
  'name',
]

def testFile():
  fieldnames = ['name', 'age']
  with open(os.path.join(DATA_DIR, 'logs.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerow({ 'name': 'Zahan', 'age': 23 })

class Simulator:
  """
  Simulates a webservice receiving requests and logging each one
  """

  def __init__(self, logger):
    # initialize this service 5 days ago
    self.current_time = datetime.now() - timedelta(days=5)
    self.logger = logger

  def serverhit(self):
    secs_elapsed = randint(0, 10)
    self.current_time += timedelta(seconds=secs_elapsed)
    self.logger.writerow({
      'timestamp': self.current_time,
      'uid': 0,
    })

if __name__ == '__main__':
  testFile()
