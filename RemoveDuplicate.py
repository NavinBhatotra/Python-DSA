# Write a function to remove the duplicate numbers on given integer array/list.

# Example
# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]

# Solution One O(n2)
def remove_duplicates(arr):
    # TODO
    unique = []
    for i in range(len(arr)):
        flag = True
        for j in range(len(unique)):
            if arr[i] == unique[j]:
                flag = False
        if(flag == True):
            unique.append(arr[i])
    return unique

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

# Solution Two O(n)
def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]