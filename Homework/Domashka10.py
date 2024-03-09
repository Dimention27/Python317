prizers = {'Natalia', 'Maxim', 'Evgeniya', 'Alexandr', 'Matvei', 'Michail'}
matematika = {'Matvei', 'Evgeniya', 'Michail', 'Maxim', 'Natalia'}
physics = {'Maxim', 'Matvei', 'Alexandr'}
print("Все призёры: ", prizers)
s = matematika & physics
print("Призёры обеих олимпиад: ", s)
physics -= prizers
s &= prizers
q = s
print("Обновлённый список призёров по математике: ", q)