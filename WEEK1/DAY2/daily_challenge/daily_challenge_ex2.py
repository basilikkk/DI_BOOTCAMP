"""Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
Notes
Final strings won’t include words with double letters (e.g. “passing”, “lottery”)."""

str1=input("please enter a string ")
list1=list(str1)
print(list1)

unique_list1=[]
for item in list1:
    if item not in unique_list1:
        unique_list1.append(item)

print(unique_list1)
string_without_duplicates=""

for i in unique_list1:
    string_without_duplicates+=i

print(string_without_duplicates)    

