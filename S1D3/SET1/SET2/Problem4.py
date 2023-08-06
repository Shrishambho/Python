str1 = "PyNaTive"

lowercase_letters = ""
uppercase_letters = ""

for char in str1:
    if char.islower():
        lowercase_letters += char
    else:
        uppercase_letters += char

arranged_string = lowercase_letters + uppercase_letters

print(arranged_string)
