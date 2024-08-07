capitalOfCountries={

    "France": "Paris",
    "Germany": "Berlin",
    "Turkey": "Ankara",
    "UK": "Londan"
}
print(f'Capital city of France is {capitalOfCountries["France"]}')

for key,value in capitalOfCountries.items():
    print(key+ " | " +value)

for value in capitalOfCountries.values():
    print(value)

