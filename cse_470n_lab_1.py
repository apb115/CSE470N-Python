# -*- coding: utf-8 -*-
"""CSE 470N Lab 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BtrRwWgNweeD7MIApW3twqDDBxvsthmt
"""

a = 9
b = 7
print(a,b)

a,b = b,a
print(a,b)

if a > b:
  c = a+b
  d = a-b
  print(c, d)
else:
  x = a*b
  y = a/b
  print(x, y)

def example(n):
  print("i j k")
  for i in range(n):
    for j in {"Hello World"}:
      for k in "XYZ":
        print(i,j,k)
example(2)

counts = {}
counts['00'] = 477
counts['11'] = 522
counts['00'] += 1
print(counts)

name = input('Enter your name:')
print('Hello, ' + name)
age = int(input("Enter your age"))
print(name + " is " + str(age) + " years old")

name = input('Enter age limit: ')
list1 = ['Andrew', 'David', 'Pardis', 'Emily', 'Kate', 'Sarah', 'Elise', 'Johnny']
people = {}
people['Andrew'] = 20
people['David'] = 29
people['Pardis'] = 29
people['Emily'] = 19
people['Kate'] = 14
people['Sarah'] = 16
people['Elise'] = 12
people['Johnny'] = 11

i = 0
for person in people:
  if people.get(person) > 16:
    print(person + " is older than 16")
  i += 1