def fuck(n):
    if n==0 | n==1:
        return 1
    else:
        return n*fuck(n-1)
n=int(input("Enter a fucking number"))
print(f"The fucking factorial which makes you orgasm is : {fuck(n)}")

