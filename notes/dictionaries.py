dict1 = {'a':1, 'b':2, 'c':[12,13,14], 'd':{'d1':['cat','dog'],'d2':['mouse','squirrel']}}

print(dict1['d']['d1'][1])
print(dict1['a'] + dict1['b'])
print('a' in dict1) #checks only top level keys
print(dict1.values()) #all values as list
print(dict1.keys()) #all keys as list
print(dict1.items()) #all k and v as tuples

dict1.update({"e":"updated"}) #appends k v pair to the end of the dict
print(dict1.items())

popped = dict1.pop('d') #pops specified key with values and optionally stores in variable
print(dict1.items())
print(popped)