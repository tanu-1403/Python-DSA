#DAY 01: PYTHON REFRESH(loops,lists,dicts,set,functions)

#Revision
print("Hello World!", end=" ")
print("I will print on the same line.")

#"global" keyword
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#"random" module 
import random
print(random.randrange(1, 10))

#looping through a string
for x in "banana":
  print(x)
  
#placeholder and modifiers
txt = "The price is {:.2f} dollars"
print(txt.format(49.98765))

price = 59
txt1 = f"The price is {price:.2f} dollars"
print(txt1)

#escape charector
txt2 = "We are the so-called \"Vikings\" from the north."
print(txt2)

#formfeed
txt3 = "Hello \fWorld!"
print(txt3) 

#boolean
x = "Hello"
y = 0
print(bool(x))
print(bool(y))
