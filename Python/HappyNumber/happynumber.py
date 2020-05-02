def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """

    if type(n) != type(1):
        #print("Incorrect Data Type.")
        return False
    
    if(n==4):
        return False
    
    n_Sum = 0
    for nText in str(n):
        n_Sum += int(nText)**2
        
    if n_Sum == 1:
        return True
    else:
        return isHappy(n_Sum)