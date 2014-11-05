# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Jonathan Butler"

if __name__ == "__main__":
    
    location = raw_input("Please enter the location of the data.txt file: ");
    
    print "you've entered: ", location
    
    file = open("G:\data.txt","r") 
    array = []  
    for line in file:
        array.extend([int(num) for num in line.split()])
    file.close()
    
    if len(array)%10 != 0:
        print("ERROR: Incorrect number of integers.")
        exit()
    
    sliceMatrix1 = slice(0,(len(array)/2))
    sliceMatrix2 = slice((len(array)/2), len(array))
    
    matrix1 = array[sliceMatrix1]
    matrix2 = array[sliceMatrix2]
    
    print(array)
    print(matrix1)
    print(matrix2)
    print("////////////////////////////////////////////////////////////////////////////////////")
   