my_dict = {
    "name": "Alice",  # String
    "age": 30,        # Integer
    "is_student": False,  # Boolean
    "height": 1.65,     # Float
    "hobbies": ["reading", "coding", "hiking"],  # List
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA"
    }  # Nested dictionary
}

for key,value in my_dict.items():
        # Convert value to string if it's not already a string
    if not isinstance(value, str):
        value = str(value)
    print(key + " | " + value)


# We have to check the value if it is str...
