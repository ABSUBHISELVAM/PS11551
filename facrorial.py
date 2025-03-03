def num(n):
    if n==0 | n==1:
        return 1
    else:
        return n*num(n-1)
n=int(input("Enter a number"))
print(f"The  factorial  is : {num(n)}")

