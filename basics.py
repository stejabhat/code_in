#1
x=y=z=3
print(x)

#2
x,y,z=3,3,4
print(z)

#3
print(type(y))

#4 array
a="element"
print(a[3])

#5 display vertically
for i in a:
    print(i)

#6 length
print(len(a))

#8 finding word in a paragraph way1:
h="thala for a reason"
print("thala" in h)

#9 way 2:
if "thala" in h:
    print("Thala is present")

if "king" in h:
    print("King is present")

#10 slice
g="Ee sala cup namde"
print(g[0:6])
print(g[:7])

#11 negative indexing
print(g[-6:-1])

#12 cases
u="punith"
print(u.upper())
i="PUNITH"
print(i.lower())

#13 split
q="Punith Gowda..The Trainer_"
print(q)
print(q.strip("_"))
print(q.replace("i","e"))
print(q.split(".."))

#14 escaping character
t="my name is \"teja\" bhat"
print(t)

#15 conditions
m=10
k=20
if m>k:
    print("m is greater than k")
else:
    print("k is greater than m")

# 16 lists
li=['Raghav','kedar','shiv']
print(li)
print(li[1])
print(li[0:1])

#17 insert
li.insert(1,"leviosa")

#18 append
li.append("leela")

#19 extend,remove,pop
lis=["Swara","Madhura"]
li.extend(lis)
li.remove("leviosa")
lis.pop(1)

#20 sorting
so=["orange","mango","apple"]
so.sort()
print(so)

sor=[55,100,1,20]
sor.sort(reverse=True)
print(sor)

sd=[1,2,3,4]
sor=sd.copy()
sd.extend(sor)