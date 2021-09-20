mylist = ["appel","banana","charry","apple","cherry",6]
tropical = ["mango","pineapple","papaya"]
print(mylist)
print(len(mylist))
print(mylist[1])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:4])
print(mylist[2:])
print(mylist[-4:-1]) 
 
if "apple" in mylist:
    print("yes,'apple' is in the fruits list")

mylist[1] = "blackcurrant"
print(mylist)

mylist[1:3] = ["blackcurrant","watermelon"]
print(mylist)

mylist[1:2] = ["blackcurrant","watermelon"]
print(mylist)

mylist[1:3] = ["watermelon"]
print(mylist)

mylist.insert(2,"watermelon")
print(mylist)

mylist.append("orange")
print(mylist)

mylist.insert(1,"orange")
print(mylist)

mylist.extend(tropical)
print(mylist)

mylist.remove("mango")
print(mylist)

mylist.pop(1)
print(mylist)

mylist.pop()
print(mylist)

del mylist[0]
print(mylist)

mylist = ["appel","banana","charry","apple","cherry",6]

del mylist


thislist = ["apple","banana","cherry"]
print(thislist)

thislist.clear()
print(thislist)

thislist = ["apple","banana","cherry"]
print(thislist)

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [ x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist  = [x.upper() for x in fruits ]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)
thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1.extend(list2)
print(list1)

print(list1.count("a"))
print(list1.index(1))
print(list1.reverse())