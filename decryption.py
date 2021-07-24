key= ['EC', 'FF', 'FC', 'EB', 'FD', 'CE', 
'CD', 'BC', 'D', 'FB', 'CF', 'BE', 
'DF', 'DD', 'BF', 'DC', 'EE', 'B', 
'CB', 'EF', 'BD', 'DE', 'BB', 'ED', 
'F', 'E', 'DB', 'C', 'FE', 'CC']

encryptedtext= [4, 6, 23, 12, 21, 21, 2, 4, 9]

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(chr(decimal))  



def binaryequivalenttable(x):
  tabledict= {
        "A": "0",
        "B": "1",
        "C": "00",
        "D": "01",
        "E": "10",
        "F": "11",
       # "G": "000",
       # "H": "001",
       # "I": "010",
       # "J": "011",
       # "K": "100",
       # "L": "101",
       # "M": "110",
       # "N": "111"
    }
  return tabledict[x]

firstlevel= ''

for u in encryptedtext:
  firstlevel= firstlevel+ key[u]
#print (firstlevel)
String= ''
for i in firstlevel:
  String= String+binaryequivalenttable(i)
plaintext= ''
while (len(String)!=0):
  plaintext= plaintext + binaryToDecimal(int(String[:7]))
  String= String[7:]
print (plaintext)


