# list comprehension in list is to be reviewed


# List Built-in
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count() 	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index() 	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()   	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()  	Sorts the list


#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.


# Tuple Built-in
Method	  Description
count()	  Returns the number of times a specified value occurs in a tuple
index()	  Searches the tuple for a specified value and returns the position of where it was found


# frozen set methods
Method    	               Shortcut    Description	
copy()              	 	           Returns a shallow copy	
difference()	              -        Returns a new frozenset with the difference	
intersection()                &        Returns a new frozenset with the intersection	
isdisjoint()	        	           Returns whether two frozensets have an intersection	
issubset()	               <= OR <     Returns True if this frozenset is a (proper) subset of another	
issuperset()	           >= OR >     Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	      ^        Returns a new frozenset with the symmetric differences	
union()	                      |        Returns a new frozenset containing the union


# set methods
Method	                   Shortcut	   Description
add()	 	                           Adds an element to the set
clear()	 	                           Removes all the elements from the set
copy()	 	                           Returns a copy of the set
difference()	               -	   Returns a set containing the difference between two or more sets
difference_update()	          -=	   Removes the items in this set that are also included in another, specified set
discard()	 	                       Remove the specified item
intersection()	               &	   Returns a set, that is the intersection of two other sets
intersection_update()	       &=	   Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                   Returns whether two sets have a intersection or not
issubset()	                   <=	   Returns True if all items of this set is present in another set
 	                           <	   Returns True if all items of this set is present in another, larger set
issuperset()	               >=	   Returns True if all items of another set is present in this set
 	                           >	   Returns True if all items of another, smaller set is present in this set
pop()	 	                           Removes an element from the set
remove()	 	                       Removes the specified element
symmetric_difference()	       ^	   Returns a set with the symmetric differences of two sets
symmetric_difference_update()  ^=	   Inserts the symmetric differences from this set and another
union()	                       |	   Return a set containing the union of sets
update()	                   |=	   Update the set with the union of this set and others