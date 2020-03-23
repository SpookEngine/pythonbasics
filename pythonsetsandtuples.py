#Sets
print('SETS' + '\n')
vowels = set('aeiou')
print(vowels)
#While a list can have duplicate values, a SET CANT HAVE DUPLICATES
vowels.add('u')
print(vowels)
#word = input('Enter a word')
word = "headphones"

#Union operation --> a collection of all the unique characters of the two sets
union_set = vowels.union(set(word))
print(union_set)

#Difference between two sets
difference_set = vowels.difference(set(word))
print(difference_set)

#Common values between two sets
intersection_set = vowels.intersection(set(word))
print(intersection_set)

print('\nTUPLES' + '\n')
#Tuples - once they have been created they cannot be modified
vowels_tuple = ('a', 'e', 'i', 'o', 'u')
print(vowels_tuple)
print(vowels_tuple[2])
