#!/usr/bin/env python3

def evolve(world, steps):
    # implement this function
    
    
    #define some useful functions
    
    def live_in_next_cycle(pic,line_pos,string_pos):
        """
        No need to consider border because it is taken care of in the draw_next function

        Parameters
        ----------
        pic : List
            list of string that shows the current state
        line_pos : Int
            index of the line we are on
        string_pos : Int
            index of the position in a string

        Returns Bool
        -------
        Case 1: populated - if it has two or three neighbours, return True, else False
        Case 2: unpopulated - if it has two neighbouts return True, else return False

        """
        #case1
        if pic[line_pos][string_pos] == '#':
            #count =-1 because i will "unintentionally" add 1 in the nested for loop
            #at [linepos][stringpos]
            count = -1
            
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if pic[line_pos+i][string_pos+j]=='#':
                        count += 1
            
            
            if count==2 or count == 3:
                return True
            else:
                return False
            
            
        #case2    
        elif pic[line_pos][string_pos] == ' ':
            
            count = 0
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if pic[line_pos+i][string_pos+j]=='#':
                        count += 1
            
            
            
            if count == 3:
                return True
            else:
                return False
            
            
        else:
            raise Warning(f"the current char is {pic[line_pos][string_pos]} at pos{line_pos}-{string_pos}")
            
            
            
        
    
    def draw_next(pic):
        """
        

        Parameters
        ----------
        pic : List
            List of strings

        Returns
        -------
        next_state : List
            returns a List of strings, shows the next state of input state

        """
        next_state = []
        for i,line in enumerate(pic):
            if i==0 or i==len(pic)-1:
                #we are at border, just append current line to next_state
                next_state.append(line)
                continue #skip current line
            
            string=""
            for j,character in enumerate(line):
                if j==0 or j==len(line)-1:
                    #we are at border, just append current char to string
                    string += pic[i][j]
                    continue
                
                #we are in middle of a line, check if this spot contains live cell
                #in the next cycle
                
                if live_in_next_cycle(pic,i,j)==True:
                    string += '#'
                else:
                    string += ' '
                
            #append the completed string of next state to next_state
            next_state.append(string)
            
            
        return next_state
    
    
    
    
    def count_hash(param):
        """
        Done        

        Parameters
        ----------
        param : List
            List of strings

        Returns
        -------
        count : Int
            returns how many times '#' occured

        """
        count=0
        for string in param:
            for i in string:
                if i=='#':
                    count += 1
        
        
        return count
    
    #------------------end of define useful functions-----------
    
    
    
    
    
    #Main
    #start by handle warnings
    
    VALID_CHAR = ['#','-','|',' ']
    
    if not isinstance(steps,int):
        raise Warning #input steps is not integer
    
    if steps<=0:
        raise Warning #negative input steps
        
    if world == ():
        raise Warning #empty world
    
    pic = list(world)
    length = len(pic[0])
    
    if len(pic)<=2:
        raise Warning #unsensible size
    
    for line in pic:
        if len(line) != length or len(line)<=2:
            raise Warning #unequal line length or unsensible size
            
        for character in line:
            if not character in VALID_CHAR:
                raise Warning #invalid char
                
                
    #run the get next state function steps times        
    next_pic = []
    temp = pic
    for i in range(0,steps):            
        
        next_pic = draw_next(temp)
        temp = next_pic
        
 
    
    
    return tuple(next_pic), count_hash(next_pic)



#---------end of implementation ---------------------------------------


field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 2

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")





















