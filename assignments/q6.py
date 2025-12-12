#Write a Python program to find the first appearance of the substring 'not' and'poor' from a given string, 
#if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

string1 = input("Enter a string: ")
nott = string1.find("not")
poor = string1.find("poor")

if nott != -1 and poor != -1 and poor > nott:
    nstring = string1[:nott] + "good" + string1[poor + 4:]
else:
    nstring = string1

print("Result:",nstring)
