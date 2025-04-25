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

print("\nValues: \n")
for v in dict1.values():
    print(v)
    
print("\nKeys: \n")
for k in dict1.keys():
    print(k)
    
print("\nKeys, Values:\n")
for k,v in dict1.items():
    print(k,v)


allowed_keys = ['a', 'c'] #filter list
filtered_dict1 = {} #initialize empty dict to store filtered items

for key in dict1.keys():
    #check the filter
    if key in allowed_keys:
        filtered_dict1[key] = dict1[key]
print("\nFiltered dict1:\n")
print(filtered_dict1.items())
        
dict2 = dict1 #hard copy, changing dict1 changes dict2
dict3 = dict1.copy() #changing dict1 in future wont change dict3

word_list = ["hello","I'm", "hi", "goodbye" ]

dict4 = {}
#add words filtered by first char to dictionary
for word in word_list:
    first_char = word[0]
    if first_char not in dict4:
        dict4[first_char] = [word]
    else:
        dict4[first_char].append(word)

print(dict4)