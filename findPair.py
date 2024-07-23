# Find the pairs of Sum (Don't repeat same element)
# Example arr is [4,6,3,6,1,8] and target is 9
# output = [1,2] , [2,3], [4,5]

# Solution One
def findPairs(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]: continue
            if arr[i] + arr[j] == target:
                print(f"Index is {i,j}")

arr = [4,6,3,6,1,8]       
target = 9        

findPairs(arr, target)

# Solution Two
def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
arr = [4,6,3,6,1,8]       
target = 9      
indices = two_sum(arr, target)
print(f"Indices of the two numbers are: {indices}")