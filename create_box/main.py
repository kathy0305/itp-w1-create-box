def create_box(height, width, character):
    box =""
    line = character * width + "\n"
    for i in range (height):        # This defines the number of rows
       box = box + line
    return box   #  char passed multiplied by width passed 
            
        
##create_box (3,4,'*')
##create_box (5,2,'@') 
##create_box(3,24,'x')



            


if __name__ == '__main__':
  create_box(3, 4, '*')
