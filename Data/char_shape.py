###############################################################################
# Georgia Doing (doingg@union.edu)
#
# Print an ascii L shape
###############################################################################

# function definition
def char_shape(wide, high, character):
    """Use the given shape to print an L shape
    with given rows and columns"""
    
	# print a single column of a character
    row = character + "\n"
    # print up to second to last row
    all_rows = row * (high - 1)
    
    # end without a newline so 'L' is connected
    print(all_rows, character, sep = "")

    # now print horizontal part
    print( wide* character)


# call char_shape to test

char_shape(6, 4, "#")
