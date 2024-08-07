def is_palindrome(input_string):
  return input_string == input_string[::-1]

def find_palindromes_with_btc(start, end):
  palindromes_with_btc = []
  for num in range(start, end + 1):
    if is_palindrome(str(num)): #we put str(num)!
      palindrome_with_btc = str(num) + ".btc" 
      palindromes_with_btc.append(palindrome_with_btc)
  return palindromes_with_btc

# Example usage:
start_num = 100
end_num = 200
palindromes_with_btc = find_palindromes_with_btc(start_num, end_num)
print(palindromes_with_btc)
