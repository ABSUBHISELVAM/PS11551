def duck(n):
    if n==0 | n==1:
        return 1
    else:
        return n*duck(n-1)
n=int(input("Enter a ducking number"))
print(f"The ducking factorial which makes you orgasm is : {duck(n)}")

