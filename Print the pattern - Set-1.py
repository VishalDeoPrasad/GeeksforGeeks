def printPat(n):
    res=""
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            res+=i*(str(j)+" ")
        res+="$"
    print(res)

printPat(5) 