import re

f = open("input2.txt", "r")
indexSum = 0
for index, x in enumerate(f):

        maxBlue = 0
    for y in re.findall(r'\d+ blue',x):
        temp = int(re.sub(r'blue', "", y))
        if(temp > maxBlue):
            maxBlue = temp

        maxGreen = 0 
    for y in re.findall(r'\d+ green',x):
        temp = int(re.sub(r'green', "", y))
        if(temp > maxGreen):
            maxGreen = temp

        maxRed = 0 
    for y in re.findall(r'\d+ red',x):
        temp = int(re.sub(r'red', "", y))
        if(temp > maxRed):
            maxRed = temp

    if(not flag):
        indexSum += index + 1

print(indexSum)
