def jewelinstone(jewels,stones):
    s=set()
    count = 0
    for ch in jewels:
        s.add(ch)
    for ch in stones:
        if ch in s:
            count+=1
    return count

jew="1234"
stones="112234"
print(jewelinstone(jew,stones))
"""
## Pythonic Way

```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        jewels = set(jewels)

        return sum(ch in jewels for ch in stones)
```
"""