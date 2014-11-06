__author__="Jonathan Butler"

if __name__ == "__main__":
    
    location = raw_input("Please enter the location of the data.txt file. For example 'C:\...Desktop\data.txt' or '/home/.../Desktop/data.txt': ");    
    location = "G:\data.txt"    
    try:
        file = open(location,"r") 
        array = []  
        for line in file:
            array.extend([int(num) for num in line.split()])
        file.close()
    except:
        print("ERROR: file could not be found/read.")
        exit()
    
    if len(array)%10 != 0:
        print("ERROR: Incorrect number of integers in data.txt file.")
        exit()
    
    sliceMatrix1 = slice(0,(len(array)/2))
    sliceMatrix2 = slice((len(array)/2), len(array))

    matrix1 = array[sliceMatrix1]
    matrix2 = array[sliceMatrix2]
    
    matrixA = []
    tmp=0
    for i in range(0,5):
        matrixA.append([])
        for j in xrange((len(array)/2)/5):
            matrixA[i].append(matrix1[tmp])
            tmp=tmp+1
            
    matrixB = []
    tmp=0
    for i in range((len(array)/2)/5):
        matrixB.append([])
        for j in xrange(0,5):
            matrixB[i].append(matrix2[tmp])
            tmp=tmp+1
        
    matrixC = []
    tmp=0
    for i in range(0,5):
        matrixC.append([])
        for j in xrange(0,5):
            matrixC[i].append(1)
            tmp=tmp+1
    
    print(array)
    print(matrixA)
    print(matrixB)
    print(matrixC)