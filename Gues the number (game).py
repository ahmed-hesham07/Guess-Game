import random

RandomNumber = int(random.randrange(1,10))

print ('guess the number between 1 and 10')

trials = 5

UserGuess =int()

while  trials > 0 and UserGuess != RandomNumber:
  
 UserGuess = int(input())
 
 if UserGuess > RandomNumber: 
   
   print('TOO HIGH')
   
   print('try again')
   
   trials -= 1
 
 
 elif UserGuess < RandomNumber:
 
     print('TOO LOW')
 
     print('try again ')
 
     trials -= 1
 
 
 elif UserGuess == RandomNumber:
 
       print('CONGRATULATIONS! YOU WON!') 
 
       continue

