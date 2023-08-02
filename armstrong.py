a=int(input("Enter number:"))
org=a
sum=0
while a>0:
    sum=sum+(a%10)**3
    a=a//10
    print(sum)
if sum==org:
    print("armstrong number")
else:
    print("Not Armstrong number")
