
a=input("enter the name")
b=0
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        b+=1
print("total vowels={0}".format(b))
print(a)
