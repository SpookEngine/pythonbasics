#Function definitions always begin with the def keyword. Specifying :str is not required, but can help users decide the type of data expected as argument. We can also specify the return type with -> dict
def count_vowels(sentence:str) -> dict:
  """Return list of vowels found in sentence"""

  vowels = set('aeiou')
  vowel_count = {}

  for ch in list(sentence):
    if ch in vowels:
      vowel_count.setdefault(ch,0)
      vowel_count[ch] += 1

  return vowel_count

print(count_vowels('Is there life on Mars?'))
print(count_vowels('Yes there is!'))

#We can also define default values for arguments: after the argument name and type we can specify the default value like in the case of letters here
def find_common_letters(sentence:str, letters:str='python') -> set:
  """Return set of characters common to both arguments"""
  return set(sentence).intersection(set(letters))

print(find_common_letters('Is there life on Mars?', 'python'))
print(find_common_letters('Is there life on Mars?'))
print(find_common_letters('Is there life on Mars?', 'snake'))

#Keyword assignment - order doesn't matter if you use it like this, specifying the keywords:
print(find_common_letters(letters='snake', sentence='Is there life on Mars?'))
