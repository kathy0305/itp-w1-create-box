"""This is the entry point of the program."""


def create_box(height, width, character):
    for i in range (height):        # This defines the number of rows
       print (character * width)   # print char passed multiplied by width passed 
            
        
##create_box (3,4,'*')
##create_box (5,2,'@')   
            


if __name__ == '__main__':
    create_box(3, 4, '*')
