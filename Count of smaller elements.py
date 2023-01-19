def countOfElements1(a, n, x):
    cnt = 0
    for i in range(n):
        if a[i] <= x:
            cnt += 1
    return cnt

def countOfElements(a, n, x):
    return len([a[i] for i in range(n) if a[i] <= x])

print(countOfElements([1,2,4,5,8,10], 6, 9))
