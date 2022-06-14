def sumOfArrays(ArrayOne, ArrayTwo):
    i=len(ArrayOne) - 1
    j=len(ArrayTwo) - 1
    ArrayThree = []
    ResultArray = []
    dozens = 0
    if i > j:
        k=i-j
        for d in range(k):
            ArrayTwo.insert(0, 0)
    elif i < j:
        k=j-i
        for d in range(k):
            ArrayOne.insert(0, 0)
    
    while i>= 0:
        sum = ArrayOne[i] + ArrayTwo[i] + dozens
        if sum <= 9:
            ArrayThree.append(sum)
            i-=1
            dozens=0
        else:
            modulus = sum%10
            dozens=int(sum/10)
            ArrayThree.append(modulus)
            i-=1
    ArrayThree.append(dozens)
    ResultLen = len(ArrayThree) - 1
    while ResultLen >= 0:
        ResultArray.append(ArrayThree[ResultLen])
        ResultLen-=1
    print(ResultArray)
    

def main():
    sumOfArrays([1,3,5,8], [9,3,5,3])

if __name__ == "__main__":
    main()
        