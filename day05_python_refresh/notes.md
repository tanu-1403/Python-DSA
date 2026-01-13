Array Methods
Python has a set of built-in methods that you can use on lists/arrays.

Method	     Description
append()	 Adds an element at the end of the list
clear()	     Removes all the elements from the list
copy()	     Returns a copy of the list
count()	     Returns the number of elements with the specified value
extend()	 Add the elements of a list (or any iterable), to the end of the current list
index()	     Returns the index of the first element with the specified value
insert()	 Adds an element at the specified position
pop()	     Removes the element at the specified position
remove()	 Removes the first item with the specified value
reverse()	 Reverses the order of the list
sort()	     Sorts the list


#DATETIME

Directive	      Description	                                          	
%a	              Weekday, short version	                                    	
%A                Weekday, full version                                     		
%w	              Weekday as a number 0-6, 0 is Sunday		
%d	              Day of month 01-31		
%b	              Month name, short version		
%B	              Month name, full version		
%m	              Month as a number 01-12		
%y	              Year, short version, without century		
%Y	              Year, full version		
%H	              Hour 00-23		
%I	              Hour 00-12		
%p	              AM/PM		
%M	              Minute 00-59		
%S	              Second 00-59		
%f	              Microsecond 000000-999999		
%z	              UTC offset		
%Z	              Timezone		
%j	              Day number of year 001-366		
%U	              Week number of year, Sunday as the first day of week, 00-53		
%W	              Week number of year, Monday as the first day of week, 00-53		
%c	              Local version of date and time	
%C	              Century		
%x	              Local version of date		
%X	              Local version of time	
%%	              A % character	
%G	              ISO 8601 year	
%u	              ISO 8601 weekday (1-7)		
%V	              ISO 8601 weeknumber (01-53)		


#JSON

Python	JSON
dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null


#RegEx Functions

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string


#Metacharacters

Character	Description	                                                                  Example	
[]	        A set of characters		                                                       "[a-m]"
\	        Signals a special sequence (can also be used to escape special characters)	   "\d"	
.	        Any character (except newline character)	                                   "he..o"	
^	        Starts with	                                                                   "^hello"	
$	        Ends with	                                                                   "planet$"	
*	        Zero or more occurrences	                                                   "he.*o"	
+	        One or more occurrences	                                                       "he.+o"	
?	        Zero or one occurrences	                                                       "he.?o"	
{}	        Exactly the specified number of occurrences	                                   "he.{2}o"	
|	        Either or	                                                                   "falls|stays"	
()	        Capture and group	 	


#Flags

Flag	        Shorthand	 Description	
re.ASCII	      re.A	     Returns only ASCII matches	
re.DEBUG		             Returns debug information	
re.DOTALL	      re.S	     Makes the . character match all characters (including newline character)	
re.IGNORECASE	  re.I	     Case-insensitive matching	
re.MULTILINE	  re.M	     Returns only matches at the beginning of each line	
re.NOFLAG		             Specifies that no flag is set for this pattern	
re.UNICODE	      re.U	     Returns Unicode matches. This is default from Python 3
re.VERBOSE	      re.X	     Allows whitespaces and comments inside patterns. Makes the pattern more readable	


#Special Sequences

Character	Description	                                                                                   Example	
\A	        Returns a match if the specified characters are at the beginning of the string	               "\AThe"	
\b	        Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	           r"\bain" r"ain\b"	

\B	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	            r"\Bain"
r"ain\B"	

\d	        Returns a match where the string contains digits (numbers from 0-9)	                            "\d"	
\D          Returns a match where the string DOES NOT contain digits	                                    "\D"	
\s	        Returns a match where the string contains a white space character	                            "\s"	
\S	        Returns a match where the string DOES NOT contain a white space character	                    "\S"	
\w	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	                                                                                "\w"	
\W	        Returns a match where the string DOES NOT contain any word characters	                        "\W"	
\Z	        Returns a match if the specified characters are at the end of the string	                  "Spain\Z"	


#Sets

Set	        Description	Try it
[arn]	    Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	
 
#Formatting Types
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format