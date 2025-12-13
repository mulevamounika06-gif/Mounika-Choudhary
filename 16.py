#Fucntion: fuction is a group of statements which returns some result.

1. Function with paramenters and without return value
2. Function with paramenters and with return value
3. Function without paramenters and without return value
4. Function without paramenters and wit return value

1.def isPrime1(num):
    count=0
    a=False
    for i in range(1, (num//2)+1):
        if num%i==0:
            count=count+1
    if count==1:
       a=True
    
b=isPrime1(11)
if b==True:
    print("Prime number")
else:
    print("Not a prime number")

2.def isPrime1(num):
    count=0
    a=False
    for i in range(1, (num//2)+1):
        if num%i==0:
            count=count+1
    if count==1:
       a=True
    return a
    
b=isPrime1(12)
if b==True:
    print("Prime number")
else:
    print("Not a prime number")

