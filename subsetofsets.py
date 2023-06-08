# You are given two sets,  and . 
# Your job is to find whether set  is a subset of set .

# If set  is subset of set , print True.
# If set  is not a subset of set , print False.
# Input Format
# The first line will contain the number of test cases, . 
# The first line of each test case contains the number of elements in set .
# The second line of each test case contains the space separated elements of set .
# The third line of each test case contains the number of elements in set .
# The fourth line of each test case contains the space separated elements of set .
# Constraints


# Output Format
# Output True or False for each test case on separate lines.
test_cases = int(input())
for _ in range(test_cases):
    n_A = int(input())
    setA = (input().strip().split())[:n_A]
    n_B = int(input())
    setB = (input().strip().split())[:n_B]
    setA,setB = set(setA),set(setB)
    print(setA.issubset(setB))   

