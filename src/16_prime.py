import sys
from math import ceil, sqrt

target = sys.argv[1]

def isPrime(target):
  arr = [False, False]
  for i in range(2, target+1):
    arr.append(True)
  for i in range(2, ceil(sqrt(target+1))):
    if arr[i]:
      for j in range(i**2, target+1, i):
        arr[j] = False
    if not arr[target]:
      return False
  return arr[target]

print(f'{target} is prime' if isPrime(int(target)) else f'{target} is not prime')
