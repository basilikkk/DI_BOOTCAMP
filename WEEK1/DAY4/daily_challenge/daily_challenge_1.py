""""Instructions
Given a “Matrix” string:

    7ii
    Tsx
    h%?
    i #
    sM 
    $a 
    #t%
    ^r!


The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
A grid means that you could potentially break it into rows and columns, like here:

7	i	i
T	s	x
h	%	?
i		#
s	M	
$	a	
#	t	%
^	r	!


Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
To reproduce the grid, the matrix should be a 2D list, not a string



To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

Using his technique, try to decode this matrix.

Hints:
Use
● lists for storing data
● Loops for going through the data
● if/else statements to check the data
● String for the output of the secret message

Hint (if needed) : Look at the remote learning “Matrix” videos

"""


matrix_str = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
"""

#convert the string to 2dim array
matrix = [list(line) for line in matrix_str.strip().split('\n')]


message = []
current_word = []


rows = len(matrix)
cols = len(matrix[0])


for col in range(cols):
    for row in range(rows):
        char = matrix[row][col]
        if char.isalpha():  
            current_word.append(char)
        else:
            if current_word:  # If there is an ongoing word
                message.append(''.join(current_word))
                current_word = []
    

# Join the message with spaces between words
decoded_message = ' '.join(message)
print("Decoded Message:", decoded_message)
