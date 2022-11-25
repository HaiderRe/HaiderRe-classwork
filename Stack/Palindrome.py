mystring = input("Please enter a word or phrase to be tested").upper()
s = ""
stack = []
for c in mystring:
    if 64 < ord(c) < 91:
        s = s + c
        stack.append(c)

newString = ""
for _ in range( len(stack)):
    newString = newString + stack.pop()
if s == newString:
    print("Palindrome")
else:
    print("Not Palindrome")