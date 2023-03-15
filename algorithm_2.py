#Split in Half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split(str):
    n = int(len(str) /2)
    str1 = str[:n:]
    str2 = str[n+1::]
    return str2 + str1

a = split("sedtfghbdfhtr21")
print(a)

#Unique Characters in String
#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

def unique_chars(str):
    for i in range(len(str) + 1):
        if str[i] in str[i+1::]:
            return True
        else:
            return False

a = unique_chars("springs")
print(a)

