def printPat(n):
    #Code here
    for i in range(n):
        for j in range(n, 0, -1):
            for _ in range(n, i, -1):
                print(j, end=" ")

        print('$', end='')

printPat(3)

