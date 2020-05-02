from HappyNumber import hnTests
from MaximumSubarray import maximumsubarray
from SingleNumber import singlenumber

def allTests():
    print("Starting to run all tests.\n")
    failedTests = 0
    # HAPPY NUMBER TESTS
    print("Starting Happy Tests")
    if hnTests.happyNumberTests():
        print ("-Failed Happy Tests.")
        failedTests += 1
    print("\n")
    
    # MAXIMUM SUBARRAY TESTS
    print("Starting Maximum SubArray Tests")
    if hnTests.happyNumberTests():
        print ("-Failed Maximum SubArray Tests.")
        failedTests += 1
    print("\n")
    
    # SINGLE NUMBER TESTS
    print("Starting Single Number Tests")
    if hnTests.happyNumberTests():
        print ("-Failed Single Number Test.")
        failedTests += 1
    print("\n")

    if failedTests == 0:
        print("Passed All Tests!")    
    return True