# File path to the nameslist.txt file
file_path = "nameslist.txt"

# 1. Read the file line by line
with open(file_path, 'r') as file:
    lines = file.readlines()

# 2. Read only the 5th line of the file
fifth_line = lines[4].strip() if len(lines) >= 5 else None

# 3. Read only the first 5 characters of the file
first_five_chars = lines[0][:5]

# 4. Read all the file and return it as a list of strings, then split each word
with open(file_path, 'r') as file:
    content = file.read().strip().split()

# 5. Find occurrences of "Darth", "Luke", and "Lea"
name_counts = {
    "Darth": content.count("Darth"),
    "Luke": content.count("Luke"),
    "Lea": content.count("Lea"),
    "vasili": content.count('Vasili')
}

# 6. Append your first name at the end of the file
my_first_name = "Vasili"
with open(file_path, 'a') as file:
    file.write("\n" + my_first_name)

# 7. Append "SkyWalker" next to each occurrence of "Luke"
with open(file_path, 'r+') as file:
    file_content = file.read()
    file_content = file_content.replace("Luke", "Luke SkyWalker")

    # Move pointer to the beginning and rewrite the entire file
    file.seek(0)
    file.write(file_content)

# Output results
print("Fifth line of the file:", fifth_line)
print("First five characters of the file:", first_five_chars)
print("Occurrences in the file:", name_counts)
print(my_first_name)
