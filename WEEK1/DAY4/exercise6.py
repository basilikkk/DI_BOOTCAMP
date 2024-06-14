"""Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

Create a function called show_magicians(), which prints the name of each magician in the list.
Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
Call the function make_great().
Call the function show_magicians() to see that the list has actually been modified.
"""

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel'] 
def show_magicians(list):
    for i in range(len(list)):
        print(list[i])


show_magicians(magician_names)

def make_great(list):
    for i in range(len(list)):
        list[i]=list[i]+" "+"the Great"

make_great(magician_names)
show_magicians(magician_names)        