def sort_words(words):
  sorted_words = sorted(words.split(), key=str.casefold)
  return ' '.join(sorted_words)


unsorted_string = "This is a random sentence"
sorted_string = sort_words(unsorted_string)
print(sorted_string)
