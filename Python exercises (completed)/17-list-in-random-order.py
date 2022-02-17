import random
a1=(input('First student name: '))
a2=(input('Second student name: '))
a3=(input('Third student name: '))
a4=(input('Name of fourth student '))
list= [a1, a2, a3, a4]
r=random.shuffle (list)
print(f'The order of school presentation will be :\n {list}')