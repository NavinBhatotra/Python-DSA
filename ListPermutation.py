# Write program to check list1 and list2 are same if it's a permutation then return true or else false.

# Example 
# list1 = [1,2,3] list2 = [2,1,3]
# Output:- True

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
list1 = [1,2,3] 
list2 = [2,1,3]
print(permutation(list1, list2))