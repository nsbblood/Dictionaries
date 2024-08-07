def sum_of_digits(number):
  sum_of_digits = 0
  while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
  return sum_of_digits

# Example usage:
num = 12345
result = sum_of_digits(num)
print(f"The sum of digits in {num} is: {result}")
