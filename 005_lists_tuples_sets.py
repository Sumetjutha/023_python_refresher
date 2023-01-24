l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

print(l[0])
print(l[2])

l[0] = 'John'
print(l)

l.append('Smith')
print(l)

l.remove("John")
print(l)

s.add('Smith')
s.add('Smith')
print(s)