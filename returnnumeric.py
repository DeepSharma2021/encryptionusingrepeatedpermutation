returnvalue= []
def numeric_value(data, table,length):
  while len(data)!=0:
    if len(data)<length:
      returnvalue.append(table.index(data))
      data= ''
    else:
      returnvalue.append(table.index(data[:length]))
      data= data[length:]
  return returnvalue

  
