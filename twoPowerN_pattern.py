from math import pow

def matchLength(binary, n):
    spaceLeft = n - len(binary)
    newBinary = spaceLeft*"0"
    newBinary += binary
    print(newBinary)

def binPattern(n):
    for i in range(int(pow(2, n))):
        
        num = bin(i)[2:]
        
        matchLength(num, n)



def binRecursivePattern(n, i=0):
    if (i == pow(2,n)):
        return
    elif (i < pow(2,n)):
        num = bin(i)[2:]
        matchLength(num, n)
        binRecursivePattern(n, i+1)


n = int(input("Enter number: "))

binRecursivePattern(n)