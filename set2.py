set1={10,20,30,40,50}
set2={20,35,45,60,80}

unionSets=set1.union(set2)
print(sorted(unionSets))

intersectionSet=set1.intersection(set2)
print(intersectionSet)

differenceSet=set1.difference(set2)
print(differenceSet)

sementricSet=set1.symmetric_difference(set2) #It will not include if you have a value in both of them
print(sementricSet)

