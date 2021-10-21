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

    string_LC = ""

    LC_one = string_input[:X] # take first X letters of string_input

    LC_two = string_input[X:] # take everything but first X letters of string_input

    string_LC = LC_two + LC_one # move LC_two in front of LC_one (simulating circulation to the left)


    return string_LC


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

    string_RC = ""

    RC_one = string_input[-X:] # take the last X letters of string_input

    RC_two = string_input[:-X] # take everything but the last X letters of string_input

    string_RC = RC_one + RC_two # move RC_one (the last X letters) in front of RC_two (simulating circulation to the right)

    return string_RC


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
   
    REV_ONE = string_input[(starting_position - 1): ((starting_position - 1) + length)]    # finds the reversed chunk

    letter = len(REV_ONE)-1                                #goes to last position on name
    reverse_REV_ONE = ""
    while letter>= 0:
        reverse_REV_ONE = reverse_REV_ONE + REV_ONE[letter]
        letter -=1                                    
   
    REV_TWO = string_input[0:starting_position-1]         #putting the reversal back into the string
   
    REV_THREE = string_input[starting_position + (length - 1) : ]
   
    string_output = REV_TWO + reverse_REV_ONE + REV_THREE
   
    return string_output
   

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
        MC_332R, BOXCUTTER (S = 3, string_input = BOXCUTTER, L = 3, X = 3, D = R): "NOT SURE HOW THIS ONE WORKS"
    """
   
    MC_MIDDLE = string_input[(starting_position - 1): ((starting_position - 1) + length)]
   
    if direction == 'right':
       
        MC_MIDDLE_manipulated = ''
       
        MC_MIDDLE_one = MC_MIDDLE[-X:]              # take the last X letters of string_input
       
        MC_MIDDLE_two = MC_MIDDLE[:-X]              # take everything but the last X letters of string_input

        MC_MIDDLE_manipulated = MC_MIDDLE_one + MC_MIDDLE_two   # move RC_one (the last X letters) in front of RC_two (simulating circulation to the right)
       
    elif direction == 'left' :

        MC_MIDDLE_manipulated = ''
       
        MC_MIDDLE_one = MC_MIDDLE[:X]               # take first X letters of string_input

        MC_MIDDLE_two = MC_MIDDLE[X:]               # take everything but first X letters of string_input

        MC_MIDDLE_manipulated = MC_MIDDLE_two + MC_MIDDLE_one   # move LC_two in front of LC_one (simulating circulation to the left)
   
   
    MC_begin = string_input[ : starting_position - 1]
   
    MC_end = string_input[(starting_position - 1) + length : ]
   
    string_output = MC_begin + MC_MIDDLE_manipulated + MC_end
   
    return string_output 


def main():                                                                                                                                     # Define the main (the main menu)
   
    
    
           
if __name__ == '__main__':
    main()
