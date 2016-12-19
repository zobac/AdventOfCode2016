from sys import stdin
from collections import defaultdict


def question1():

 with open('q12Input.txt', 'r') as f:
  lines = f.readlines()

 registers = defaultdict(int)

 counter = 0
 while counter < len(lines):
     line = lines[counter]
     if line.startswith('cpy'):
         operation, frm, to = line.split()
         try:
             registers[to] = int(frm)
         except:
             registers[to] = registers[frm]

     elif line.startswith('inc'):
         operation, frm = line.split()
         registers[frm] += 1

     elif line.startswith('dec'):
         operation, frm = line.split()
         registers[frm] -= 1

     elif line.startswith('jnz'):
         operation, x, y = line.split()
         try:
             # check that x is not zero
             flag = int(x)
         except:
             flag = registers[x]

         # check that x is not zero
         if flag != 0:
             counter += int(y)
             continue
     counter += 1

 return registers['a']


def question2():

 with open('q12Input.txt', 'r') as f:
  lines = f.readlines()

 registers = defaultdict(int)
 registers['c'] = 1

 counter = 0
 while counter < len(lines):
     line = lines[counter]
     if line.startswith('cpy'):
         operation, frm, to = line.split()
         try:
             registers[to] = int(frm)
         except:
             registers[to] = registers[frm]

     elif line.startswith('inc'):
         operation, frm = line.split()
         registers[frm] += 1

     elif line.startswith('dec'):
         operation, frm = line.split()
         registers[frm] -= 1

     elif line.startswith('jnz'):
         operation, x, y = line.split()
         try:
             # check that x is not zero
             flag = int(x)
         except:
             flag = registers[x]

         # check that x is not zero
         if flag != 0:
             counter += int(y)
             continue
     counter += 1

 return registers['a']

if __name__ == "__main__":

    print(question1())

    print(question2())
