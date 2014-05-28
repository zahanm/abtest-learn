
from random import choice

FIRST_NAMES = {
  'm': [
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
  ],
  'f': [
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
  ],
}

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

def makeupone(gender: str) -> str:
  assert gender in FIRST_NAMES.keys()
  return choice(FIRST_NAMES[gender]) + ' ' + choice(LAST_NAMES)

if __name__ == '__main__':
  print(makeupone())
