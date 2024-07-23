# Find a number from a Array
# Will use basic Linear Search approach

def findNumberInArray(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: 
            return print(f"Target index is {i}")
    print(f"Target Not Found")
    
arr = [2,46,475,24,68,24,86]
target = 46
findNumberInArray(arr, target)