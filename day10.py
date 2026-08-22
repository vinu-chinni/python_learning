#important problems
#1. print numbers from 1 to 10 

for x in range(1,11):
    print(x, end=' ')
print()
print()

#2. print even numbers from 5 to 30 and above list
list=[4,3,5,2,5,2,9,1,7,4,6,8]
for x in range(1,11):
    if x%2==0:
        print(x, end=' ')
print( )
print( )
for x in list:
    if x%2==0:
        print(x , end=' ')

print( )
print( )



#3. print odd numbers from 1 to 30 and above list
for x in range(1,31):
    if x%2==1:
        print(x, end=' ')
print( )
print( )
for x in list:
    if x%2==1:
        print(x, end=' ')
print( )
print( )

#4. print numbers divisible by 5 from 1 to 30 and above list
for x in range(1,31):
    if x%5==0:
        print(x, end=' ')
print( )
for x in list:
    if x%5==0:
        print(x, end=' ')
print( )
print( )

#5.print numbers divisible by both 5 and 7 from 1 to 100 and above list
for x in range(1,101):
    if x%5==0 and x%7==0:
        print(x, end=' ')
print( )

for x in list:
    if  x%5==0 and x%7==0:
        print(x, end=' ')

print( )
print( )


#6. sum of numbers from 10 to 25 and above list
sum=0
for x in range(10,26):
    sum+=x
print("sum of numbers from 10 to 25 is: ",sum)
print( )

#7. multiplication table of a number
n=int(input("Enter a number for multiplicatin:"))
for i in range(1,21):
    print(f'{n}x{i}={n * i}')
print( )

#8. factorial 
n=int(input("Enter a number for factorial:"))
product = 1
for x in range(1,n+1):
    product*=x
print(f'Factorial of{n}is{product}')
print( )
print( )

#9. fibonacci 
n=int(input("enter the fibonacci number"))
a=0
b=1
for x in range(n):
    print(a, end=' ')
    a,b=b+a,b
print( )
print( )

#10. reverse a string




#11. count vowels in a string
s = input("Enter a string: ")
count = 0

for i in s:
    if i in "aeiou":
        count += 1

print("Vowels:", count)
print( )
print( )

#12. count z's and y's in a string
s = input("Enter a string: ")

print("z:", s.count("z"))
print("y:", s.count("y"))
print( )
print( )


#13. check whether a number is prime number or not
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
print( )
print( )
