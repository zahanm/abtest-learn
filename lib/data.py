
import csv
from datetime import datetime, timedelta
import os.path
from random import randint

import names

NUMBER_OF_HITS = 20
DATA_DIR = '../data'
FIELDNAMES = [
  'timestamp',
  'uid',
  'name',
]

def run():
  with open(os.path.join(DATA_DIR, 'logs.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, FIELDNAMES)
    writer.writeheader()
    s = Simulator(writer)
    for i in range(NUMBER_OF_HITS):
      s.serverhit()

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
      'name': names.makeupone(),
    })

if __name__ == '__main__':
  run()
