g = int(input())
f = int(input())
def fib():

  a,b = 1,1
  while True:
    yield a
    a,b = b,a+b

import itertools

a1=(list(itertools.islice(fib(), f+g)))
print(a1[g::])