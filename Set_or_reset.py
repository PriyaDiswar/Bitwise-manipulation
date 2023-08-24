#check ith bit of a number whether it is true or not(0 or 1)

n=int(input("Enter number:"))
s=int(input("enter the bit position to be checked:"))
if(n&(1<<s)):
    print("bit is 1")
else:
    print("bit is 0")
