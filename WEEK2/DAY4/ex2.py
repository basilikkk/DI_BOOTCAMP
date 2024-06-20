import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Parse the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
salary = data['company']['employee']['payable']['salary']
print(f"Salary: {salary}")

# Step 3: Add a new key “birth_date” at the same level as the “name” key
data['company']['employee']['birth_date'] = '1990-01-01'

# Step 4: Save the updated dictionary as JSON to a file
with open('updated_sample.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Updated JSON data has been saved to 'updated_sample.json'")
