array = [1,2,3,4,5]

dvalue = 17

def rotate(a,d):
  for i in range(d):
    temp_variable = a[0]
    a.pop(0)
    a.append(temp_variable)
   
  return a
print(rotate(array, dvalue))
