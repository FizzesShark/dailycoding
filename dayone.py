def solve(arr, n):
    exists = set()
    for i in arr:
        if i in exists:
            return True
        else:
            exists.add(n - i)
    return False
test = [10, 15, 3, 2]
n = 17
print(solve(test, n))
