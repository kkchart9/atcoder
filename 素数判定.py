import math

def prime_check(N):
  b = min(N-1, int(math.sqrt(1 * N)))
  for i in range(2,b+1):
    if (N % i == 0):
      return False
  return True

for i in range(1,100):
  if prime_check(i):
    print(i)
