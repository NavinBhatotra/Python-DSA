# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example
# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']

def pair_sum(myList, sum):
    # TODO
    lst = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            total = myList[i] + myList[j]
            if total == sum:
                lst.append(f"{myList[i]}+{myList[j]}")
    return lst

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))