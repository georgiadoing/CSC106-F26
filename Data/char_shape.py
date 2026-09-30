###############################################################################
# Georgia Doing (doingg@union.edu)
#
# Draw a tree by printing characters
# Week 3 Lab
###############################################################################
 

# Draw trees out of ASCII characters.

def ascii_tree(stem, leaf):
    """Draw a tree using the given characters to represent the stem
    and leaves.
    """
    print()
    print("   " + leaf)
    print("  " + leaf * 3)
    print(" " + leaf * 5)
    print(leaf * 7)
    print("  " + stem * 3)


# call the function with various characters

ascii_tree("*", "*")
ascii_tree("n", "o")
ascii_tree("#", "^")
ascii_tree("v", "~")
ascii_tree("u", "i")