import numpy as np
import matplotlib.pyplot as plt

arr=[1,2]
arr1 = np.array([1,2,3,4])
arr2 = np.array([6,7,8,9])

arr3 = np.concatenate([arr1,arr2])

arr4, arr5,arr6,arr7 = np.split(arr3,4) #splits in equal parts
print("arr4= ",arr4)
print("arr5= ",arr5)

arr8 = np.where(arr3<5)#returns matching indices
print(arr8)

sorted = np.sort(arr3)
filter1 = sorted < 5 #makes filter 
print(filter1)

print(sorted[filter1])

even = np.linspace(0,2,5) #start,end, how many. Creates evenly spaced array
print(even)

ones=np.ones(10) #returns an array filled with ones
print(ones)


zeroes = np.zeros(10)
print(zeroes)

three_of_ones = np.full((3,7),6) #3 arrays, each with 7 pieces of 6
print(three_of_ones)

date1=np.datetime64("2025-10-10") #creates date
date2=np.datetime64("2025-10-13")
print(date1<date2) #produces bool
date3 = date1 + np.timedelta64(10,"D") #adds 10 days

print(date3)


### Matplotlib pyplot ###

plt.plot(even,even,"*") #Right click, interactive, run file in interactive mode