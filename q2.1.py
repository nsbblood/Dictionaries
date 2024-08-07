'''''def valtoBinary(userInput):
    binarInput=bin(userInput)[2,]
    return binarInput
userInputGet=input("Write a number to get it's Binary number ")
inputInt=int(userInputGet)
result=valtoBinary(inputInt)
print(f"{userInputGet}'s Binar version is {result}")'''''


def val_to_binary(user_input):
  try:
    decimal_num = int(user_input)
    binary_num = bin(decimal_num)[2:]
    return binary_num
  except ValueError:
    return "Invalid input. Please enter a number."

user_input = input("Write a number to get its binary number: ")
result = val_to_binary(user_input)
print(f"{user_input}'s binary version is {result}")


