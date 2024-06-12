"""Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
Only recreate the 1st result for:
The characters, which names contain the letter “i”.
The characters, which names start with the letter “m” or “p”."""

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]


disney_users_A=[]

for i in range(len(users)):
    disney_users_A.append(i)


disney_users_A_dict=dict(zip(users,disney_users_A))
print(disney_users_A_dict)                     

disney_users_B_dict=dict(zip(disney_users_A,users))
print(disney_users_B_dict)       


disney_users_C_dict=dict(sorted(disney_users_A_dict.items()))
print(disney_users_C_dict)



# Create disney_users_A for names containing "i"
disney_users_A_dict_i = {users: index for index, users in enumerate(users) if 'i' in users.lower()}

print(disney_users_A_dict_i)


disney_users_A_dict_mp={users:index for index,users in enumerate(users) if users.lower()[0]=='m'or users.lower()[0]=='p'}

print(disney_users_A_dict_mp)