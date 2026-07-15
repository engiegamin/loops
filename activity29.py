string = input("Please enter your on string: ")

string2 = ('')
for i in string:
    string2 = i + string2
    
print("\nThe Original string= ", string)
print("\nThe Reversed string= ", string2)