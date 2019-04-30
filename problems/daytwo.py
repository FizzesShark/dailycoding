def solve(arr):
    #Seems trivial to solve in O(2n) time, equivalent to O(n)
    #There could be a method to solve in simply O(n) time, or even less,
    #but that's too much work
    temp = []
    total = 1
    for i in arr:
        total *= i
    for i in arr:
        temp.append(int(total/i))
    return temp

def solvenodiv(arr):
    #Slightly harder, but easily doable in O(n^2) time. Again, possibility of
    #faster solutions, but that's for a later date.
    temp = []
    tempTotal = 1
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                continue
            tempTotal *= arr[j]
        temp.append(tempTotal)
        tempTotal = 1
    return temp

arr = [1, 2, 3, 4, 5]
print(solve(arr))
print(solvenodiv(arr))
