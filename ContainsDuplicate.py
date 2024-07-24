# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :
# Input: nums = [1,2,3,1]
# Output: true


def contains_duplicate(nums):
    # TODO
    seen = set()
    for num in nums:
        if num in seen: 
            return True
        else:
            seen.add(num)   
    return False

nums = [1,2,3,1]
print(contains_duplicate(nums))