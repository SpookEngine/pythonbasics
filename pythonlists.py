#Lists in python have no predeclared datatypes, they are dynamic and can handle multiple occurences of a single element and multiple types of data, f.e. integer and string together
num_list = [1, 2, 3, 4, 'five']
print(num_list)
#second element of the list:
print(num_list[1])
#second to last element of the list:
print(num_list[-2])
#lenght of the list:
print(len(num_list))


if 6 in num_list:
  print('6 found in the list!')
else:
  print('6 not found! Appending...!')
  num_list.append(6)

print(num_list)

if 6 in num_list:
  print('6 found in the list!')
else:
  print('6 not found! Appending...!')
  num_list.append(6)

num_list.remove(6)
print(num_list)

#remove the last element of the list
poppedValue = num_list.pop()
print('Popped value = %s' %poppedValue)
print(num_list)

#Insert 0 at the 0th index of the list
num_list.insert(0,0)
print(num_list)

#Extend the list with another list
num_list.extend([5,6,7,8])
print(num_list)

#Start stop and stem notation
#0 = start
#8 = stop
#3 = step
limited_num_list = num_list[0:8:3]
print(limited_num_list)

limited_num_list = num_list[::3]
print(limited_num_list)

limited_num_list = num_list[1:8:3]
print(limited_num_list)

limited_num_list = num_list[1:7:3]
print(limited_num_list)

#sentence = input("Enter a sentence: ")
#this input was used in the course
sentence = "No soup for you!"
print(sentence)
#print only a subset of a string: from -4th element to the end
print(sentence[-4:])

#print a string in the opposite direction
print(sentence[::-1])

#every second character of the string - SLICING
print(sentence[::2])

#Copying lists
another_num_list = num_list
print(another_num_list)
#The copy created a new variable, which was still pointing to the SAME DATA of the original list
num_list.append(9)
print(another_num_list)

#If we want to make a real copy, we need to use .copy() instead of '=', this will create an independent copy of a data structure

yet_another_num_list = num_list.copy()
num_list.append(10)
print(yet_another_num_list)
print(num_list)

#Range function
print(range(5))
print(list(range(5)))
#We can also use start, stop, step notation here
print(list(range(0, 10, 2)))
print(list(range(10, 0, -2)))
