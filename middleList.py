# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# Example
# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

# Solution One O(n)
def middle(lst):
    # TODO
    newList = []
    for i in range(len(lst)):
        if(i == 0 or i == len(lst)-1): continue
        newList.append(lst[i])
    return newList
myList = [1, 2, 3, 4]
print(middle(myList))

# Solution Two O(n)
def middle(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1]
 
my_list = [1, 2, 3, 4]
 
print(middle(my_list))  # Output: [2, 3]