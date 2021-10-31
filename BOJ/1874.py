import sys
sequence = []
stack = [0]
cache = []
cur = 1

N = sys.stdin.readline().rstrip()
for i in range(int(N)):
  sequence.append(int(sys.stdin.readline().rstrip()))

no = False

for num in sequence:
  # print(f'num: {num}')
  complete = False
  while not complete:
    if num > stack[-1]:
      stack.append(cur)
      cache.append('+')
      cur += 1
      # print(f'stack: {stack}')
      # print('+')
    elif num == stack[-1]:
      stack.pop()
      cache.append('-')
      # print('-, complete')
      complete = True
    else:
      print('NO')
      no = True
      break
    
  if no:
    break

if not no:
  for c in cache:
    print(c)
