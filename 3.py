# Write a program to print factors of a given number
num=int(input("enter the number:"))
for i in range(1,(num//2)+1):
  if num%i==0:
    print(i,end=" ")
