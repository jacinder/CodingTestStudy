import sys

N = sys.stdin.readline().rstrip()
for i in range(int(N)):
  line = sys.stdin.readline().rstrip()
  for word in line.split(' '):
    print(''.join(reversed(list(word))), end=' ')
  print()
