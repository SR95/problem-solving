class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==4):
            return 0
        
        n_Sum = 0
        for nText in str(n):
            n_Sum += int(nText)**2
            
        if n_Sum == 1:
            return 1
        else:
            return self.isHappy(n_Sum)