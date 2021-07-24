import random
def generate_data(x,y):
  string= ''
  for i in range(y):
    string= string + random.choice(x)
  return string
#alphabets= ['a','b','c','d','e','f']
#size= 500
#data = generate_data(alphabets, size)
#print (data)