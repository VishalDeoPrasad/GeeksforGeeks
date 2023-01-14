def checkPalindrome(num):
    return 1 if num == int(str(num)[::-1]) else 0

def PalinArray(arr ,n):
    for elm in arr:
        if checkPalindrome(elm) == 0:
            return 0
    return 1
n = 5
arr = [111,222,333,444,555]
print(PalinArray(arr, n))