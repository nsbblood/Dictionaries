def is_palindrome(num):
  return str(num) == str(num)[::-1] #check if it is palindrome

def find_palindromes(start, end):
  palindromes = []
  for num in range(start, end + 1):
    if is_palindrome(num):
      palindromes.append(num)
  return palindromes

# Example usage:
start_num = 10
end_num = 100000
palindromes_found = find_palindromes(start_num, end_num)
print(palindromes_found)
