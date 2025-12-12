#Write a Python program to add 'ing' at the end of a given string (length shouldbeat least 3).
#If the given string already ends with 'ing' then add 'ly' instead If thestring length of the given string is less than 3, 
#leave it unchanged

string1 = input("Your string : ")

if len(string1)>3:
    if string1[-3:]=="ing":
        string1 = string1 + "ly"
        print(string1)
    else:
        string1 = string1 + "ing"
        print(string1)

else:
    print(string1)
