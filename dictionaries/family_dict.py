my_family = { 'wife': { 'name': 'Julia', 'age': 32 },
              'daughter': { 'name': 'Aurelia', 'age': 2 },
              'son': { 'name': 'Lazarus', 'age': .5 },
              'father': { 'name': 'Rodney', 'age': 62 } }

# use a dictionary comprehension to produce output that looks like this:
# Krista is my sister and is 42 years old

for relationship, information in my_family.items():
  family_member = relationship
  name = (information['name'])
  age = (information['age'])

  # comprehend_my_family = ['{0}'.format(name)]
  # comprehend_my_family.append('is my')
  # comprehend_my_family.append('{0}'.format(family_member))
  # comprehend_my_family.append('and is')
  # comprehend_my_family.append('{0}'.format(age))
  # comprehend_my_family.append('years old.')
  # print(' '.join(partial for partial in comprehend_my_family))

  # also works as:
  print(name + ' is my ' + family_member + ' and is ' + str(age) + ' years old.')

