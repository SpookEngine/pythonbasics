#Dictionary - key-value pairs
customer1 = {'Name': 'Klara Kempf', 'Gender': 'Female', 'Nationality': 'German', 'Car': 'Audi A4'}
print(customer1)
print(customer1['Car'])
print(customer1['Name'])

#This was an input() method originally
sentence = 'The only way to get rid of temptation is to yield to it'

#Use a dict to count vowels in a sentence
vowels = ['a', 'e', 'i', 'o', 'u']
#new dictionary
vowel_count = {}
#initializing the dictionary
vowel_count['a'] = 0
vowel_count['e'] = 0
vowel_count['i'] = 0
vowel_count['o'] = 0
vowel_count['u'] = 0

print(vowel_count)

for char in list(sentence):
  if char in vowels:
    vowel_count[char] += 1

print(vowel_count)

#The sorted() function orders the dictionaries by the keys. k = key and v = value in this loop
for k,v in sorted(vowel_count.items()):
  print('Frequency of %s: %i' %(k,v))

#Dinamic declaration of dictionary keys.
vowels = ['a', 'e', 'i', 'o', 'u']

vowel_dinamic_count = {}

for ch in list(sentence):
  if ch in vowels:
    #The setdefault initializes a kez to a default value, in this instance, the ch key to a value of 0
    vowel_dinamic_count.setdefault(ch, 0)
    vowel_dinamic_count[ch] += 1

for k,v in sorted(vowel_dinamic_count.items()):
  print('Frequency of %s: %i' %(k,v))


#Dictionary containing Dicitonaries
customers = {}
customers['Klara'] = {'Name': 'Klara Kempf', 'Gender': 'Female', 'Nationality': 'German', 'Car': 'Audi A4'}
customers['Eric'] = {'Name': 'Eric Smith', 'Gender': 'Male', 'Nationality': 'Canadian', 'Car': 'Mazda 3'}
customers['Sofia'] = {'Name': 'Sofia Sanchez', 'Gender': 'Female', 'Nationality': 'Chilean', 'Car': 'Volkswagen Golf'}

print(customers)

#pretty print
import pprint
pprint.pprint(customers)

#Accessing the data
print(customers['Sofia']['Car'])


#We can have list objects as keys
customers['Sofia']['Car'] = ['Volkswagen Golf', 'Honda Civic']
print(customers['Sofia']['Car'])
#We can get a specific object with it's index
print(customers['Sofia']['Car'][1])
