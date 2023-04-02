#############################################
# CS 1110A - Programming in Python          #
# Module 3 - Exercise 6 - Unique Characters #
# Author: Lamech Israel                     #
# Date:   01/23/2023                        #
#############################################

def uniques(s):
    
    
    
    # If nothing was entered, exit the loop.
    if s == '':
        return False
    else:
        # Initialize the arrays and the string that will be built.
        string_array = []
        capitalized = []
        unique_characters = ""
        
        # Cycle through the inputted string for characters.
        for i in range(len(s)):
            # Make sure the character is a letter.
            if s[i].isalpha():
                # If the character is Upper Case, start this loop.
                if s[i].isupper():
                    # Check if the character is unique. If so, add it to the list.
                    similar = False 
                    for c in range(len(capitalized)):
                        if s[i] == capitalized[c]:
                            similar = True
                    if similar == False :
                        capitalized.append(s[i])
                # If the character is Lower Case, start this loop.
                else:
                    # Check if the character is unique. If so, add it to the list.
                    similar = False 
                    for c in range(len(string_array)):
                        if s[i] == string_array[c]:
                            similar = True
                    if similar == False :
                        string_array.append(s[i])
        # Sort the Lower Case and Upper Case arrays.            
        string_array.sort()
        capitalized.sort()
        # Append the Upper Case array to the Lower Case array.
        string_array += capitalized
        
        # Take all the array letter and put them into a string.
        for r in range(len(string_array)):
            unique_characters += string_array[r]
        #Print the output
        print('\nOriginal string:',s)
        print('Unique characters:',unique_characters)
        #Return True so the loop can continue
        return True 
    
    

    
Running = True
print('Unique characters in a string')
while Running:
    Running = uniques(input('\nString: '))

# Exit the loop if nothing is entered.
print('\nDone!')
exit()