#TUPLE PROGRAMS
#Print each element.
t = (10,20,30,40,50)
for i in t:
    print(i)

#Maximum and minimum.
t = (10,50,20,5,80)
print(max(t))
print(min(t))

#Count occurrences.
t = (1,2,2,3,2)
print(t.count(2))

#Check value exists.
t = (10,20,30)
x = 20
if x in t:
    print("Found")
else:
    print("Not Found")

#Tuple → List → Append → Tuple.
t = (1,2,3)
l = list(t)
l.append(4)
t = tuple(l)
print(t)

#Find index.
t = (10,20,30,40)
print(t.index(30))

# Unpack tuple.
t = (10,20,30)
a,b,c = t
print(a,b,c)

#Concatenate tuples.
t1 = (1,2)
t2 = (3,4)
print(t1+t2)

# Sum of elements.
t = (10,20,30)
print(sum(t))

#Remove duplicates.
t = (1,2,2,3,3,4)
new = ()
for i in t:
    if i not in new:
        new += (i,)
print(new)