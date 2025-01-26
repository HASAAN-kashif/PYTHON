a = input("Enter a character: ")

if a.isalpha():
    print('a is an alphabet.')
else:
    print('a is not an alphabet.')

b = input("Enter a character: ")

# Ensure the input is a single character
if  a == 1:
    ascii_code = ord(b)
    print("The ASCII code of b.",ascii_code)
else:
    print("it is not an ASCII.")