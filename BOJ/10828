import sys
# import io

command = {'push':0, 'pop':1, 'size':2, 'empty':3, 'top':4}
stack = []

N = sys.stdin.readline().rstrip()
for i in range(int(N)):
  line = sys.stdin.readline().rstrip()
  try:
    com, arg = line.split(' ')
    # print(com,arg)
  except(ValueError):
    com = line
    arg = -1
    # print(com)
  
  if command[com] == 0: # push
    stack.append(arg)
  elif command[com] == 1: # pop
    try:
      print(stack.pop())
    except:
      print(-1)
  elif command[com] == 2: # size
    print(len(stack))
  elif command[com] == 3: # empty
    print(int(len(stack) == 0))
  elif command[com] == 4: # top
    try:
      print(stack[-1]) 
    except:
      print(-1)
  
  
