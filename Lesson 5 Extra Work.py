string1 = (input("Enter a string of characters"))
string2 = (input("Enter a string of characters"))
lengthstring1 = len(string1)
lengthstring2 = len(string2)
if lengthstring1 > lengthstring2:
    print ("The length of", string1, "was greater than the length of string 2")
else:
    print ("The length of", string2, "was greater than the length of string 1")