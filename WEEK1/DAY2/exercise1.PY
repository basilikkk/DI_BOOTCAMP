#1
"""Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers."""

my_fav_numbers={11,22,33,44}
my_fav_numbers.add(55)
my_fav_numbers.add(66)
print(my_fav_numbers)
my_fav_numbers.remove(66)

friend_fav_numbers={1,2,3,4,5}

our_fav_values=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_values)