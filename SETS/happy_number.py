class Solution(object):
    def isHappy(self, n):
        s=set()
        while(True):
            sum=0
            while(n>0):
                rem = n%10
                sum = sum + (rem*rem)
                n = n/10
            if (sum==1): return True
            if(sum in s): return False
            else: s.add(sum)
            n=sum
