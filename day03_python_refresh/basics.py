# loop dictionaries
thisdict={"brand": "Ford", "model": "Mustang", "year": 1964}

for x in thisdict:
  print(x)
  
for x in thisdict:
  print(thisdict[x])
  
for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)
  
for x, y in thisdict.items():
  print(x, y)
  
#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#access in nested dictionary
print(myfamily["child2"]["name"])

#loop in nested dictionary
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
    
#variables in conditions
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
  
is_logged_in = False
if is_logged_in:
  print("Welcome back!")
  
#assign value with if...else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#multiple conditions
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#terenary operators
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

#statemnts in one line
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# match in place of if...else
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
# default value in match
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# combine charectors
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
    
# extra if condition
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

#while-continue loops
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
#return values
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)