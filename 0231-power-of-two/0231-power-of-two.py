class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1: 
            return True
        power=2
        while power<=n:
            if power==n: 
                return True
            power*=2
        return False
            