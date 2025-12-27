#walrus operator
numbers = [1, 2, 3, 4, 5]#list
count = len(numbers)
if count > 3:
    print(f"List has {count} numbers")

if (count := len(numbers)) < 3:
    print(f"List has {count} elements")

#identity operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
print(x is [1,2,3])

#data types in list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#for loop 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#customise sorting in list
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#how close it is to 50

#slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#using asterik
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits1
print(green)
print(yellow)
print(red)

#another asterik
fruits2 = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits2
print(green)
print(tropic)
print(red)

#pop() set
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#join sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#duplicates
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#frozenset()
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))