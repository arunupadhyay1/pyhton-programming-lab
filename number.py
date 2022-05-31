x = 10
if x != 0:
   if x % 2 == 0:
      print('even number')
   else:
      print('odd number')
elif x == 0:
   print('equal to zero')
elif x > 0:
  for i in range(2,x):
     if i % 2 == 0:
        print('not a prime number')
     else:
        print('prime number')
else:
   print('less than zero')
