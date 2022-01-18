#!/usr/bin/env python3
import secrets
import re

def len_pass():
    """
    function generate randomly the length of password,
    from 10 to 16 caracters
    """
    while True:
        len_pass = secrets.randbelow(17)
        if len_pass >= 10:
            break
    return len_pass

def get_password(len_password):
    """
    function generates the password with the length
    gived like parameter.
    """
    password = ""    
    while len(password) <= len_password:
        # p1 and p2, positions generate randomly
        p1 = secrets.randbelow(4)
        p2 = secrets.randbelow(len(all_strings[p1]))            
        if all_strings[p1][p2] not in password:
            password += all_strings[p1][p2]
    return password

lower_strings = "abcdefghijklmnopqrstuvwxyz"
upper_strings = "ABCDEFGHIJKLMNOPQRSTU"
number_strings = "0123456789"
symbol_strings = "!@#$%^*()[]{}?"
regex = r"[a-z]{2,}[A-Z]{2,}[0-9]{2,}[!@#\$%\^\*\(\)\[\]\{\}\?]{2,}"
all_strings = []
all_strings.append(lower_strings)
all_strings.append(upper_strings)
all_strings.append(number_strings)
all_strings.append(symbol_strings)

len_password = len_pass()

print("Generating password...")
while True:    
    password = get_password(len_password)
    # checking if password matches with password requirements
    if re.search(regex, password) != None:
        break

print(f"your password is: {password}")
# saving the password in a file.
with open("your_pass.txt","w", encoding="utf-8") as file:
    file.write(password)

print("Your password saved in \"your_pass.txt\"")
print("done!")
