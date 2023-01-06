def valueEqualToIndex(arr, n):
		return [i+1 for i in range(n) if arr[i] == i+1]
print(valueEqualToIndex([15, 2, 45, 12, 7], 5))
