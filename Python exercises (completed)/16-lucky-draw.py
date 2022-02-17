import random
a1=(input("First participant's name "))
a2=(input("second participant's name: "))
op= [a1 , a2]
escolha=random.choice (op)
print(f'The winner of the draw is: {escolha}')