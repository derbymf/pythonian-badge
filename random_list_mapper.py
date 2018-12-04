import statistics
import random
import matplotlib.pyplot as plt
import numpy as np
import re

randomNum = []

#Creates a random list of 10 numbers between 0 and 100
def randomlist(templist):
    for i in range(10):
        x = random.randint(0,101)
        templist.append(x)
    return templist

#populate the list
randomlist(randomNum)

#print the list to the console
print("random numbers:", randomNum)
#if the file is not created, create it and allow it to be written to
infile = open('random.txt', 'a+')
#read the file
infile = infile.read()

#read each number from the file and map them
randomNum = re.findall(r"[-+]?\d*\.\d+|\d+", infile)
randomNum  = list(map(int, randomNum))

#functions to do calculations withS
def Max(templist):
    Max = max(templist)
    return Max
def Min(templist):
    Min = min(templist)
    return Min
def Median(templist):
    Median = statistics.median(templist)
    return Median
def Average(templist):
    Average = statistics.mean(templist)
    return Average
def Std_Dev(templist):
    Std_Dev = statistics.stdev(templist)
    return Std_Dev

#call the list again to do calculations
randomlist(randomNum)

# Bar graph template found at
#https://pythonspot.com/matplotlib-bar-chart/
objects = ['Max', 'Min', 'Mean', 'Median', 'Standard Deviation']
height = np.arange(len(objects))
x_coord = [Max(randomNum), Min(randomNum), Average(randomNum), Median(randomNum),
Std_Dev(randomNum)]
plt.bar(height, x_coord, width = .8, color = ['blue'])
plt.ylabel('List of Random Numbers')
plt.xticks(height, objects)
plt.title('Numbers')
plt.show()

