# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:18:14 2021

@author: Deep Raj Sharma
"""
import random
from permutation import all_comb
from returnnumeric import numeric_value

def binaryequivalenttable(x):
  tabledict= {
        "0": "A",
        "1": "B",
        "00": "C",
        "01": "D",
        "10": "E",
        "11": "F",
        #"000": "G",
        #"001": "H",
        #"010": "I",
        #"011": "J",
        #"100": "K",
        #"101": "L",
        #"110": "M",
        #"111": "N"
    }
  return tabledict[x]

plaintext= "hello" 
res = ''.join(format(ord(x), 'b') for x in plaintext)
#print (len(res))
tres= ''.join(format(ord(x), 'b') for x in plaintext) 
String= ''
while len(tres)!=0:
  if len(tres)<2:
    String= String + binaryequivalenttable(tres)
    tres= ''
  else:
    String= String + binaryequivalenttable(tres[:2])
    tres= tres[2:]
alphabets = list(set(String))
key= all_comb(alphabets,2)
random.shuffle(key)
encryptedtext= numeric_value(String, key,2)
f = open("demofile2.txt", "a")
p= str(key)
q= str(encryptedtext)
print (p)
print (q)
#q= str(encryptedtext)
#f.write(str(key))
#f.write(str(encryptedtext))
#f.close()
