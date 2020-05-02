import happynumber as hn

def happyNumberTests():
    failedTests = 0
    print("--test 1: Valid Entry:is a happy number")
    if(not hn.isHappy(19)):     #should be true
        print ("---Result: Failed")
        failedTests += 1
    else:
        print("---Result: Passed")
    
    print("--test 2: Valid Entry:is not a happy number")
    if(hn.isHappy(20)):        #should be false
        print ("---Result: Failed")
        failedTests += 1
    else:
        print("---Result: Passed")

    print("--test 3: Valid Entry:is a happy number")
    if(not hn.isHappy(23)):     #should be true
        print ("---Result: Failed")
        failedTests += 1
    else:
        print("---Result: Passed")
    
    print("--test 4: Valid Entry:is a happy number")
    if(not hn.isHappy(100)):    #should be true
        print ("---Result: Failed")
        failedTests += 1
    else:
        print("---Result: Passed")
    return failedTests