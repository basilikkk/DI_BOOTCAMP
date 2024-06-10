"""Recap – What is a float? What is the difference between an integer and a float?
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
Can you think of another way to generate a sequence of floats?"""


#float is a type for numbers with a point

a = [1.5] 
for i in range(2, 6):  
    a.append(i) 
    if (i+0.5)==5.5:
        break
    a.append(i + 0.5)


print(a)

#second option


int_list = list(range(2, 6))
floats_list = [i+0.5 for i in range(1, 5)]
mixed_list = int_list + floats_list
mixed_list.sort()
print(mixed_list)