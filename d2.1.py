import time
my_dict = {
    "name": "Alice",  # String
    "age": 30,        # Integer
    "is_student": False,  # Boolean
    "height": 1.69,     # Float
    "hobbies": ["kitap okuma", "film izleme", "saç çekme"],  # List
    "address": {
        "street": "Kusadasi Caddesi",
        "city": "Aydin",
        "state": "Guzel sehir"
    }  # Nested dictionary
}

my_dict["name"]="Eliii"

my_dict["Hot Girl"]="Eliii"

for key,value in my_dict.items():
    time.sleep(0.9)
        # Convert value to string if it's not already a string
    if not isinstance(value, str):
        value = str(value)
    print(key + " | " + value)


# We have to check the value if it is str...
