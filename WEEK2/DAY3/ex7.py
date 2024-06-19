from faker import Faker

# Initialize Faker
fake = Faker()

# Create an empty list called users
users = []

def add_user(users_list, num_users=1):
    for _ in range(num_users):
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        users_list.append(user)

# Example usage
add_user(users, 5)  # Add 5 users
for user in users:
    print(user)
