zoo = ('elephant', 'baa', 'panda', 'tiki bird',)

print(zoo.index('panda'))

[print('There are sheep in the zoo. FUCK!') for item in zoo if 'baa' in item]
[print('There are snakes in the zoo. FUCK!') for item in zoo if 'snake' in item]

(trunk, wool, bamboo, tiki_room) = zoo
print (trunk, bamboo)

zoo = list(zoo)

zoo.extend (['snake', 'monkey', 'penguin'])

zoo = tuple(zoo)
print(zoo)
