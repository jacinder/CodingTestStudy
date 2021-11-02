from collections import deque
import sys
queue = deque()
command = {'push':1, 'front':2, 'back':3, 'size':4, 'empty':5, 'pop':6}

N = sys.stdin.readline().rstrip()
for i in range(int(N)):
  data = sys.stdin.readline().rstrip()
  try:
    com = command[data]
  except:
    data,char = data.split(' ')
    com = command[data]
  
  if com == 1: # push
    queue.append(char)
  elif com == 2: # front
    try:
      print(queue[0])
    except:
      print(-1)
  elif com == 3:
    try:
      print(queue[-1])
    except:
      print(-1)
  elif com == 4:
    print(len(queue))
  elif com == 5:
    print(int(len(queue)==0))
  elif com == 6: # pop
    try:
      print(queue.popleft())
    except:
      print(-1)
