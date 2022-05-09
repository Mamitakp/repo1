from typing import Counter


list1={'a':1,'b':2,'c':{1:1,2:{'a':1,'b':2,'c':'hello'}}}
x=list1['c'][2]['c']
print(x)
print(Counter(x))