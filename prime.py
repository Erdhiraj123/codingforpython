#To Prime in Interval

for x in range(2,20):
    count=0
    for i in range(2,x//2+1):
        if x%i==0:
            count=count+1
            break
    if count==0:
        print(x)
        
# To Check wheathe a number prime or not

prime=int(input("Enter a number:"))
count=0
for x in range(2,prime//2+1):
    if prime%x==0:
        count=count+1
if count==0:
    print("Prime number")
else:
    print("Not prime ")
