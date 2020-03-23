import random
import time
from time import gmtime as the_time

#print(time.gmtime())
for i in range(5):

  random_num = random.randint(2,7)
  print(random_num)
  time.sleep(random_num)

  this_second = the_time().tm_sec
  print('This second: %s' %this_second)

  if this_second%3 == 0:
    print('%s is divisible by 3!' %this_second)
    continue;
  elif this_second%2 ==0:
    print('%s is divisible by 2!' %this_second)
  else:
    print('Default')

  print('Iteration complete!')
