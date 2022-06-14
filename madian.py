def madianOfSortedArray(Array):
    HolderArray = []
    k = 0
    index = 0
    while k <= len(Array) - 1:
        for i in Array:
            isLesser = True
            for j in Array:        
                if i > j:
                   isLesser = False
            if isLesser == True:
                HolderArray.append(i)
                index = Array.index(i)
        k+=1
        Array[index] = 10000000000
    madian = (HolderArray[len(HolderArray) - 1] + HolderArray[0]) / 2
    print(HolderArray)
    print("the madian of this array is :" + str(madian))
    

def main():
    madianOfSortedArray([11,2, 5, 9, 10, 42, 55, 98, 0])

if __name__ == "__main__":
    main()