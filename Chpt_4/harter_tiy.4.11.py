pizzas=['pepperoni','cheese','sausage']
friend_pizzas=pizzas[:]
pizzas.append('pineapple')
friend_pizzas.append('ham')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('\n')
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
