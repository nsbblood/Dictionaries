def decimal_to_binary(decimal_num):
  binary_num = bin(decimal_num)[2:]  # Remove '0b' prefix
  return binary_num

# Example usage:
number = 42
binary_representation = decimal_to_binary(number)
print(binary_representation)  # Output: '101010'
