import sys


N = sys.stdin.readline().rstrip()
for i in range(int(N)):
  vps = True
  stack = []

  line = sys.stdin.readline().rstrip()
  for parenthes in line:
    if parenthes == '(':
      stack.append('(')
    else: # parenthes == ')'
      try:
        stack.pop()
      except:
        vps = False
        break
  if len(stack) != 0:
    vps = False
  
  print("YES" if vps else "NO")
