def char_freq(s):
    freq = [0] * 123
    for ch in s:
        freq[ord(ch)] += 1
    
    # Loop through the string to keep the original order
    for ch in s:
        # Check if the frequency is greater than 0
        if freq[ord(ch)] > 0:
            print(f"{ch}->{freq[ord(ch)]}")
            # Set frequency to 0 so we don't print duplicates
            freq[ord(ch)] = 0

## Pythonic Way

from collections import Counter

s = "character"

freq = Counter(s)

for ch,count in freq.items():
    print(ch,":",count)