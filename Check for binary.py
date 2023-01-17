def isBinary1(str):
    #code here
    for b in str:
        if b not in ['0','1']:
            return 0
    return 1

def isBinary(str):
    #code here
    return next((0 for b in str if b not in ['0','1']), 1)
    
    

print(isBinary("01111001101011500"))

