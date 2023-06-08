# You are given a set  and  other sets. 
# Your job is to find whether set  is a strict superset of each of the  sets.
# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.
# Example 
# Set is a strict superset of set. 
# Set is not a strict superset of set. 
# Set is not a strict superset of set.
# Input Format
# The first line contains the space separated elements of set . 
# The second line contains integer , the number of other sets. 
# The next  lines contains the space separated elements of the other sets.
# Constraints



# Output Format
# Print True if set  is a strict superset of all other  sets. Otherwise, print False.

setA = set(input().strip().split())
n = int(input())
sets = []
for _ in range(n):
    sets.append(set(input().strip().split()))
val ="f"
for i in sets:
    if i.issubset(setA):
        if len(setA - i)!=0:
           val="t" 
        else:
            val="f"
            break
    else:
        val="f"  
        break      

if(val=="t"):
    print("True")
else:
    print("False") 


 
