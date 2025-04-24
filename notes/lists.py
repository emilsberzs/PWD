l = [1,2,3,4,5]

l.insert(2,2.5) #before index, value
l.append(6)
print(l)
popped =l.pop()
print(popped)
l.reverse()
l.sort()
l.sort(reverse=True)
l.remove(2.5)
del l[1]
l.clear()

for val in range(10):
    l.append(val)
    
def printList(list):
    for value in list:
        print(str(value) + "\n")
        
printList(l)

print(l)
print(len(l))
print([v for v in l if v%2==0 or v>7]) # Oneline list iterator

first_three = l[:3]
last_three = l[-3:]
second_to_third = l[1:3]
print(first_three)
print(last_three)
print(second_to_third)

def printMax(list):
    """Finds and prints max value in the list"""
    max = 0
    for v in list:
        if v > max:
            max = v
    print(f"Largest value in this list is {max}.")

printMax(l)
l.insert(2,15)
printMax(l)


