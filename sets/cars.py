showroom = set()
showroom.add('Chevrolet SS')
showroom.add('Mazda Miata')
showroom.add('GMC Yukon XL Denali')
showroom.add('Porsche Cayman')
# print(showroom)

# print (len(showroom))

showroom.update(['Jaguar F-Type', 'Ariel Atom 3'])
# print (showroom)

showroom.remove('GMC Yukon XL Denali')
# print (showroom)

junkyard = set()
junkyard.update([
                'Mazda Miata',
                'Chevy Caprice',
                'Isuzu Trooper',
                'Saturn SC2',
                'Porsche Cayman'
                ])
# print(junkyard)

def intersect(showroom, junkyard):
  return list(set(showroom) & set(junkyard))
# print(intersect(showroom, junkyard))

showroom = showroom.union(junkyard)
# print(showroom)

showroom.discard('Isuzu Trooper')
print(showroom)
