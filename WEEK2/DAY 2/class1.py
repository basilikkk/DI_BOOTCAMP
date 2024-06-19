"""Given a list of numbers, write a function that returns the sum of every number. BUT you can have a malicious string inside the list.

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]"""


def sum1(list:list):
    sum2=0
    for i in range(len(list)):
        if isinstance(list[i],(int,float)):
            sum2+=list[i]
    print(sum2)


my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

sum1(my_list)

