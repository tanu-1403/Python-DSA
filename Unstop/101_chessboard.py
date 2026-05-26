'''Above is the standard representation of a chessboard.

This could be imagined as a 2D cartesian plane, with the x axis being represented by the alphabets and y axis by the numbers.

Given coordinates in the form of string, print if that cell is white or black.'''

def determine_color(s):
    n1=ord(s[0])
    n2=int(s[1])
    n3=n1+n2
    if n3%2==0:
        return "Black"
    else:
        return "White"
        
    pass

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the input string
    
    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()

#COMPLETE SUBMISSION