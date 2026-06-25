s1=input("Enter String one:")
s2=input("Enter String two:")

def isAnagram(str1,str2):

    if len(str1) != len(str2):
        return False

    freq = [0] * 123

    for ch in str1:
        freq[ord(ch)] += 1

    for ch in str2:
        freq[ord(ch)] -= 1

    for i in range(97,123):
        if freq[i] != 0:
            return False

    return True
print(isAnagram(s1,s2))