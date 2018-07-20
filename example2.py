# function to chcek if the number is prime
def isPrime(number):
    for i in range(2,number):
        if(number % i != 0):
            return false
      return true
 
if(isPrime(7)):
    print("7 is prime number")
else:
    print("7 is not prime number")

#random.randint(a, b )==> return a random integer N such that a <= N <= b.

num=random.randint(0,9)
if(isPrime(num)):
    print (num "is prime number")
elif
    print (num "is not prime number")
