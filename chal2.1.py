def is_palindrome(input_string):
  return input_string == input_string[::-1]  #easiest way to check if it is a palindrome or not

# Test cases
string1 = "racecar"
string2 = "hello"

print(is_palindrome(string1)) 
print(is_palindrome(string2))  
