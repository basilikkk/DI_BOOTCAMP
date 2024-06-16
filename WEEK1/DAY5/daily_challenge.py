"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension"""

comma_sep_str=input('please enter a comma separated sequence of words ')
list_comma_str=comma_sep_str.split(',')
ordered_list=sorted(list_comma_str)
comma_sep_str_ordered=', '.join(ordered_list)
print(comma_sep_str_ordered)

#using List Comprehension
comma_sep_str_1=input('please enter a comma separated sequence of words ')
list_comma_str_1=[word.strip() for word in comma_sep_str_1.split()]
ordered_list_1=sorted(list_comma_str_1)
comma_sep_str_ordered_1=", ".join(ordered_list_1)
print(comma_sep_str_1)

