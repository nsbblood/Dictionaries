colorsList=set(["red","blue","yellow"])

color="Orange"

if color in colorsList:
    print("It is in the color list!")
else:
    print(f"{color} is not in the color list")

letterList=set(["a","b","c"])
letterList.add("y")
print(letterList)

letterList2=set(['a','b','c'])
letterList2.add('y')
letterList2.add("z")
print(sorted(letterList2))

#in sets " " and '' worked very well for me...

