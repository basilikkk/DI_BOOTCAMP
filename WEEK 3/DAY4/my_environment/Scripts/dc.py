import requests
import sqlite3
import random

# Step 1: Fetch data from the REST Countries API with filtered fields
url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population"
response = requests.get(url)
countries = response.json()

# Step 2: Select 10 random countries
selected_countries = random.sample(countries, 10)

# Step 3: Store the selected countries into a database
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('countries.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        name TEXT,
        capital TEXT,
        flag TEXT,
        subregion TEXT,
        population INTEGER
    )
''')

# Insert selected countries into the table
for country in selected_countries:
    name = country.get('name', {}).get('common')
    capital = country.get('capital', [None])[0]  # capital is a list
    flag = country.get('flags', {}).get('svg')
    subregion = country.get('subregion')
    population = country.get('population')
    
    cursor.execute('''
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, capital, flag, subregion, population))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("10 random countries have been inserted into the database.")