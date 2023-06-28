# 1. Buatlah sebuah fungsi untuk mencetak bilangan prima dari 1 hingga n (n adalah parameter input).

def isPrime(num) :
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    i = 3
    while i*i <= num: 
        if num % i == 0: return False 
        i += 2
    return True
 



n = input('Enter n: ')
print('You Entered:', n)

for i in range(int(n)):
    if(isPrime(i)):
        print(i)
