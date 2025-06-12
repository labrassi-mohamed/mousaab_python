# Draw a pyramid using '*'
# The number of stars increases by 2 on each level starting by 1 
# The number of spaces decreases by 1 on each level starting by 4

rows = 5

for i in range(1, (rows + 1)):
    # Print Spaces
    print(" "*(rows - i), end="")   
    
    # Print *
    print("*"* (2*i - 1))
