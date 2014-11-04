# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Jonathan Butler"

if __name__ == "__main__":
    
    location = raw_input("Please enter the location of the data.txt file: ");
    
    print "you've entered: ", location
    
    file = open(location)
    
    print file.read()
   
