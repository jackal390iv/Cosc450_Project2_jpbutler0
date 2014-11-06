__author__="Jonathan Butler"

if __name__ == "__main__":
    
    location = raw_input("Please enter the location of the data.txt file. For example 'C:\...Desktop\data.txt' or '/home/.../Desktop/data.txt': ");  
    """location = "G:\data.txt"""    
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
        for k in range((len(array)/2)/5):
            matrixA[i].append(matrix1[tmp])
            tmp=tmp+1
            
    matrixB = []
    tmp=0
    for i in range((len(array)/2)/5):
        matrixB.append([])
        for k in range(0,5):
            matrixB[i].append(matrix2[tmp])
            tmp=tmp+1
                           
    matrixC = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                    
    for i in range(5):
        for j in range(5):
            for k in range((len(array)/2)/5):
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
                                
    location = raw_input("Please enter the save location of the output.txt file (please note that this will overwrite other files). For example 'C:\...Desktop\data.txt' or '/home/.../Desktop/data.txt': ");  
    """location = "G:\output.txt"""    
    try:
        file = open(location,"w") 
        
        file.write("Matrix A\n")
        for scan in matrixA:
            file.write(str(scan)+"\n")
    
        file.write("\nMatrix B\n")
        for scan in matrixB:
            file.write(str(scan)+"\n")
            
        file.write("\nMatrix C\n")
        for scan in matrixC:
            file.write(str(scan)+"\n")
    
        file.close()
    except:
        print("ERROR: file could not be written to.")
        exit()
   
    