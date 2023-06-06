#set
s1={1,3}
s2={1,2,3,"hi", (1,2,3,4,)}
l=[1,4,6,7]
s3= set(l)
print(s3)

s1.add(2)
print(s1)

s1.update([2,3,4])
print(s1)

s1.discard(4) #discard removes the specified items from the set
print(s1)

# s1.remove(4) #remove will raise an error if item is not present
# print(s1)

#set operations
a={1,2,3,4}
b={4,5,6,7}

#union
print(c=a.union(b))

#Dictionary
