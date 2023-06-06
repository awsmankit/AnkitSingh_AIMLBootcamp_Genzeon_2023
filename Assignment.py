#1.Strings
string = " Ankit Singh"
print(len(string))
print(string.upper())
print(string.lower())
print(string.strip())
print(string.capitalize())
print(string.split(" "))
print(string.replace("Ankit", "Atul"))
print(string.find("Ankit"))
print(string.isdigit())
print(string.partition("Singh"))
print(string.istitle())
print(string.casefold())
print(string.center(5))
print(string.zfill(2))

print("-----------------------------------------")
#2. list
list1 = [1, 2, 3, 5, 10, 7, 6]
list1.append(4)
print(list1)
list1.remove(2) # pop the element
print(list1)
list1.sort()
print(list1)
list1.copy()
print(list1)
x= list1.index(3)
print(x)
list1.pop(3) # pop on the index
print(list1)

