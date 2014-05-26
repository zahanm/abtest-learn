
from random import choice

FIRST_NAMES = [
  'James',
  'John',
  'Robert',
  'Michael',
  'William',
  'David',
  'Richard',
  'Charles',
  'Joseph',
  'Thomas',
  'Mary',
  'Patricia',
  'Linda',
  'Barbara',
  'Elizabeth',
  'Jennifer',
  'Maria',
  'Susan',
  'Margaret',
  'Dorothy',
]

LAST_NAMES = [
  'Smith',
  'Johnson',
  'Williams',
  'Brown',
  'Jones',
  'Miller',
  'Davis',
  'García',
  'Rodríguez',
  'Wilson',
  'Martínez',
  'Anderson',
  'Taylor',
  'Thomas',
  'Hernández',
  'Moore',
  'Martin',
  'Jackson',
  'Thompson',
  'White',
  'López',
  'Lee',
  'González',
  'Harris',
  'Clark',
]

def makeupone() -> str:
  return choice(FIRST_NAMES) + ' ' + choice(LAST_NAMES)

if __name__ == '__main__':
  print(makeupone())
