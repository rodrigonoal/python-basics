print ('Welcome to Pypet!')

owl={
  'name':'Owley',
  'age': 5,
  'weight': 2.7,
  'hungry': True,
  'photo': '{(o)v(o)}'
}

mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3 )~~~~',
}

pets = [owl, mouse]


def feed(pet):
  if pet['hungry'] == True:
    pet['hungry'] = False
    pet['weight'] = pet['weight'] + 1
    print ('omnomom!!')
  else:
    print (pet['name'] + ' is not hungry!')

for pet in pets:
    print ('------------------------------')
    print ('Hello ' + pet['name'] + '!')
    print (pet['photo'])
    feed(pet)
    print ('Weight: ' + str(pet['weight']))
    print ('Weight: ' + str(pet['weight']))
    print ('------------------------------')