'''
Names: Michael Powell, Jane Tortorella, Jordan Werner, and Cal Cunnion
Narrative: 
    This program takes in different functions to manipulate inputted strings by the user. There are six different functions:
    - LS_X: Shifts all of the characters of a string by "X" places to the left. The leftmost characters are deleted by "X" #s to the right.
    - RS_X: Shifts all of the characters of a string by "X" places to the right. The rightmost characters are deleted by "X" #s to the left.
    - LC_X: Circulates the leftmost characters to the right-hand side of the string by X characters.
    - RC_X: Circulates the rightmost characters to the left-hand side of the string by X characters.
    - REV_SL: Reverses the order of the characters starting at position S with a length L in a string.
    - MC_SLXD: Circulates X characters from starting position S with a length of L, in the direction D in a string.
    
Log:
    Log 1.0/Release
        All functions worked except for REV_SL and MC_SLXD because of an error in turning the arguments into a list.
    
    Log 1.1
        Error fixed in Log 1.0. The code is functional except when the user inputs a non-manipulative value.
        
    Log 1.2
        Code ensures that the user must insert specific inputs for the functions to work. Documentation added.
    
Bugs: 
    Issue with inputting an argument greater than the length of the line.
    
Finished on 10/25/2021
'''


def LS_X(string_input, X):
    """
        Summary and Description of Function:
   
        This function shifts all of the characters of a string by "X" places to the left.
        The leftmost characters are deleted in replacement of "X" hashtags ("#") to the right.
       
        Parameters:
       
        string_input (string): The string inserted by the user.
        X (int): The number of characters shifted in the string.
       
        Returns:
        string_LS (string): The manipulated string done by the LS_X function.
       
        Example:
        LS-4, ELECTRONICS (X = 4, string_input = ELECTRONICS): TRONICS####
    """
   
   
    ls_one = string_input[X: ]                                                                  # Takes the end chunk of the string_input starting at position 'X'
    
    counter = 1                                                                                 # Defines a counter equal to one
    hashtags_list = []                                                                          # Defines an empty list
    
    while counter <= X :                                                                        # The while loop appends 'X' hashtags into a list
       
        hashtags_list.append('#')
       
        counter = counter + 1
   
    hashtags_string = ''.join(hashtags_list)                                                    # The hashtags list is converted into a string
   
    string_output = ls_one + hashtags_string                                                    # The string output is defined by adding the end chunk to the hashtags
   
   
    return string_output                                                                        # Returns the string output



def RS_X(string_input, X):
    """
        Summary and Description of Function:
    
        This function shifts all of the characters of a string by "X" places to the right. 
        The rightmost characters are deleted in replacement of "X" hashtags ("#") to the left.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters shifted in the string.
        
        Returns:
        string_RS (string): The manipulated string done by the RS_X function.
        
        Example:
        RS-3, CHAIRS (X = 3, string_input = CHAIRS): ###CHA
    """


    rs_one = string_input[ : -(X) ]                                                         # Takes the beginning chunk of the string up to position 'X' from the right
   
    counter = 1                                                                             # Defines a counter equal to one
    hashtags_list = []                                                                      # Defines an empty list
    
    while counter <= X :                                                                    # The while loop appends 'X' hashtags into a list
       
        hashtags_list.append('#')
       
        counter = counter + 1
   
    hashtags_string = ''.join(hashtags_list)                                                # The hashtags list is converted into a string   
   
    string_output = hashtags_string + rs_one                                                # The string output is defined by combining the hashtags with the beginning chunk
   
   
    return string_output                                                                    # Returns the string output
    
    
    
def LC_X(string_input, X):
    """
        Summary and Description of Function:
        
        This function circulates the leftmost characters to the right-hand side of the string by X characters.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters circulated in the string.
        
        Returns:
        string_LC (string): The manipulated string done by the LC_X function.
        
        Example:
        LC-2, NOTEBOOK (X = 2, string_input = NOTEBOOK): TEBOOKNO
    """


    LC_one = string_input[ : X]                                                             # Takes the first X letters of string_input

    LC_two = string_input[X : ]                                                             # Takes everything but first X letters of string_input

    string_LC = LC_two + LC_one                                                             # Moves LC_two in front of LC_one (simulating circulation to the left)


    return string_LC                                                                        # Returns the output



def RC_X(string_input, X):
    """
        Summary and Description of Function:
        
        This function circulates the rightmost characters to the left-hand side of the string by X characters.
        
        Parameters:
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters circulated in the string.
        
        Returns:
        string_RC (string): The manipulated string done by the RC_X function.
        
        Example:
        RC-5, WHITEBOARD (X = 5, string_input = BLACKBOARD): BOARDBLACK
    """
    

    RC_one = string_input[-X:]                                                              # Takes the last X letters of string_input

    RC_two = string_input[:-X]                                                              # Takes everything but the last X letters of string_input

    string_RC = RC_one + RC_two                                                             # Moves RC_one (the last X letters) in front of RC_two (simulating circulation to the right)


    return string_RC                                                                        # Returns the output



def REV_SL(string_input, starting_position, length):
    """
        Summary and Description of Function:
   
        This function reverses the order of the characters starting at position S with a length L.
       
        Parameters:
       
        string_input (string): The string inserted by the user.
        starting_position (int): Character starting position.
        length (int): The number of characters in the string to be reversed.
       
       
        Returns:
        string_REV (string): The manipulated string done by the REV_SL function.
       
        Example:
        REV_24, PEOPLE (S = 2, L = 4, string_input = PEOPLE): PLPOEE
    """
   
   
    REV_ONE = string_input[(starting_position - 1): ((starting_position - 1) + length)]     # Takes the chunk that needs to be reversed

    letter = len(REV_ONE) - 1                                                               # Take the last character of the string
    reverse_REV_ONE = ""                                                                    # Defines an empty string
    
    while letter >= 0 :                                                                     # Reverses the string
        reverse_REV_ONE = reverse_REV_ONE + REV_ONE[letter]
        letter -=1                                    
   
    REV_TWO = string_input[0 : starting_position - 1]                                       # Defines the beginning chunk before the reversed string
   
    REV_THREE = string_input[starting_position + (length - 1) : ]                           # Defines the end chunk after the reversed string
   
    string_output = REV_TWO + reverse_REV_ONE + REV_THREE                                   # Adds the beginning chunk with the reversed string with the end chunk
   
    return string_output                                                                    # Returns the output
   
   

def MC_SLXD(string_input, starting_position, length, X, direction):
    """
        Summary and Description of Function:
   
        This function circulates X characters from starting position S with a length of L, in the direction D.
       
        Parameters:
       
        string_input (string): The string inserted by the user.
        X (int): The number of characters circulated in the string.
        length (int): Length of the string being circulated fro m S.
        starting_position (int): Character starting position.
        direction (string): Direction, right or left (R, L)
       
        Returns:
        string_MC (string): The manipulated string done by the MC_SLXD function.
       
        Example:
        MC_432R, BOXCUTTER (S = 4, string_input = BOXCUTTER, L = 3, X = 2, D = R): BOXUTCTER
    """
   
   
    MC_MIDDLE = string_input[(starting_position - 1): ((starting_position - 1) + length)]   # Defines the string needed to be manipulated
   
    if direction == 'R':                                                                    # If the direction is to the right, then:
       
        MC_MIDDLE_manipulated = ''                                                          # Define an empty string
       
        MC_MIDDLE_one = MC_MIDDLE[-X : ]                                                    # Take the last X letters of string_input
       
        MC_MIDDLE_two = MC_MIDDLE[ : -X]                                                    # Take everything but the last X letters of string_input

        MC_MIDDLE_manipulated = MC_MIDDLE_one + MC_MIDDLE_two                               # Move RC_one (the last X letters) in front of RC_two (simulating circulation to the right)
       
       
    elif direction == 'L' :                                                                 # If the direction is to the left, then :

        MC_MIDDLE_manipulated = ''                                                          # Define an empty string               
       
        MC_MIDDLE_one = MC_MIDDLE[:X]                                                       # Take first X letters of string_input

        MC_MIDDLE_two = MC_MIDDLE[X:]                                                       # Take everything but first X letters of string_input

        MC_MIDDLE_manipulated = MC_MIDDLE_two + MC_MIDDLE_one                               # Move LC_two in front of LC_one (simulating circulation to the left)
   
   
    MC_begin = string_input[ : starting_position - 1]                                       # Find the chunk before the manipulated string
   
    MC_end = string_input[(starting_position - 1) + length : ]                              # Find the chunk after the manipulated string
   
    string_output = MC_begin + MC_MIDDLE_manipulated + MC_end                               # Combine the beginning chunk with the manipulated string with the end chunk
   
    return string_output                                                                    # Return the output



def main():
    
    # Description on what to insert into the program
    
    print('Please insert five lines of strings.\nEach string needs to consist of commands separated by slashes and at the end, a command string to operate on.')
    print('Example: LS-1/RS-1/OHIO.')
    
    while True :                                                                            # A while TRUE loop to ensure the user does not insert inappropriate functions.
        repeat = 'no'                                                                       # Set repeat equal to 'no'
        
        # Ask the user to insert five different lines
        
        line_one = input('\nInput the first line: ')
        line_two = input('Input the second line: ')
        line_three = input('Input the third line: ')
        line_four = input('Input the fourth line: ')
        line_five = input('Input the fifth line: ')
        
        lines = [line_one, line_two, line_three, line_four, line_five]                      # Convert the lines into a single list
        
        output_list = []                                                                    # Define an empty list called output_list
        
        for line in lines :                                                                 # A for loop to run each line in lines
            line = line.split('/')                                                          # Convert the line into a list separated at the slash
            
            counter = 0                                                                     # Set a counter equal to zero
            string_input = line[len(line) - 1]                                              # Define the string_input at the end of the line
            
            while counter < len(line) - 1 :                                                 # A while loop using the counter to run each command
                command = line[counter]                                                     # Set the command equal to the position of the line set by the counter
                
                command = command.split('-')                                                # Convert the command into a list separated at the hyphen
                
                # The different possible functions
                
                if command[0] == 'LS' :
                    string_input = LS_X(string_input, int(command[1]))
                
                elif command[0] == 'RS' :
                    string_input = RS_X(string_input, int(command[1]))
                
                elif command[0] == 'LC' :
                    string_input = LC_X(string_input, int(command[1]))
                
                elif command[0] == 'RC' :
                    string_input = RC_X(string_input, int(command[1]))
                
                elif command[0] == 'REV' :
                    arguments = list(command[1])                                            # Convert the second position of the command into a list to identify the different arguments for REV_SL
                    string_input = REV_SL(string_input, int(arguments[0]), int(arguments[1]))
                
                elif command[0] == 'MC' :
                    arguments = list(command[1])                                            # Convert the second position of the command into a list to identify the different arguments for MC_SLXD
                    string_input = MC_SLXD(string_input, int(arguments[0]), int(arguments[1]), int(arguments[2]), arguments[3])
                
                else :                                                                      # If one of the functions does not exist, break the while loop and set repeat equal to 'yes'
                    print('One of the functions inputted does not exist.\nPlease make sure the functions are either LS-X, RS-X, LC-X, RC-X, REV-SL, or MC-SLXD.')
                    repeat = 'yes'
                    break
                
                counter = counter + 1                                                       # Add the counter by one
            
            if repeat == 'yes' :                                                            # Use repeat = 'yes' to break out of the for loop
                break
            
            else :                                                                          # Append the manipulated line into the output_list
                output_list.append(string_input)
        
        
        if repeat == 'yes' :                                                                # Use repeat = 'yes' to repeat the while TRUE loop
            continue
        
        else :                                                                              # Once finished with each line, break the while TRUE loop
            break
        
        
    # Print the manipulated lines 
    
    print('The outputs for each of the five lines of strings inputted are:')                
    
    for element in output_list :
        print(element)
    
    # Terminate the program with a print statement
    
    print('Thank you for using the program. It has now been terminated...')
           
if __name__ == '__main__':
    main()
