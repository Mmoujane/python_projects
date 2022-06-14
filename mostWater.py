def MostWater(Array):
    Len = len(Array) - 1 
    position = []
    resultArray = []
    result = 0
    for i in range(Len):
        position.append(i)
    for j in Array:
        for l in position:
            resultArray.append(j * l)
    
    for q in resultArray:
        isGreater = True
        for s in resultArray:
            if q < s:
                isGreater = False
        if isGreater == True:
            result = q
    print(resultArray)
    print("the max area of water the container can contain is " + str(result))

def main():
    MostWater([1,8,6,2,5,4,8,3,7])

if __name__ == "__main__":
    main()
