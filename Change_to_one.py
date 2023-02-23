#change ith bit of a number to 1

n=int(input("Enter the number:"))
s=int(input("Enter the bit position:"))
ans=n|(1<<s)
print(ans)
