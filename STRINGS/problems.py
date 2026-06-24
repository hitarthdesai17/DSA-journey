s = input("Enter a string: ")
# Use print(s[::-1])
reversed_str = ""

for i in range(len(s)-1,-1,-1):
    reversed_str += s[i]

print(reversed_str)

str = input("Enter a string: ")
for i in range(len(str)):
    print(str[i])
# for ch in s:
#     print(ch)

# Q38. Toggle Each Alphabet Using ASCII Values

### DSA Way
def toggleCase(s):
    result = ""

    for ch in s:
        ascii_val = ord(ch)

        if 65 <= ascii_val <= 90:
            result += chr(ascii_val + 32)#Coverts to smaller case

        elif 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)#Converts to Uppercase

        else:
            result += ch

    return result

print(toggleCase("AcgDfD"))

### ASCII Range


# A-Z -> 65 to 90
# a-z -> 97 to 122


### Pythonic Way

def toggleCase(s):
    return s.swapcase()

print(toggleCase("AcgDfD"))

s1 = "hello bhai kya haal chaal"

ans = ""

arrStr = s1.split()

for word in arrStr:

    if len(word) <= 2:
        ans += word.upper() + " "

    else:
        ans += (
            word[0].upper()
            + word[1:-1]
            + word[-1].upper()
            + " "
        )

print(ans)