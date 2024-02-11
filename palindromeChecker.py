# Palindrome checker

nString = []

string = input("Enter the string: ")
string = string.lower()

for i in string:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        nString.append(i)

if nString == nString[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
