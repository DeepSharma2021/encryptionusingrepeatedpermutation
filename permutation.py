from itertools import product
def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return results

def repeated_permutation(a,b):
  repetedperm= all_repeat(a,b)
  rp= []
  for i in repetedperm:
    x1= ''
    for j in i:
      x1= x1+j
    rp.append(x1)
  return rp

def all_comb(x,y):
  d= []
  for i in range(1,y+1):
    d.extend(repeated_permutation(x,i))
  return d

