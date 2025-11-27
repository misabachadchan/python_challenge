#12
n=list(map(int,input("Enter numbers:").split()))
if n == sorted(n):
    print("True")
else:
    print("False")
