secret=7
attempt=0

while True:
    n=int(input("Enter your guess:"))
    attempt+=1

    if(n==secret):
        print("Congratulations you guess the number")
        break 
    elif n>secret:
        print("Too high")
    else:
        print("Too loo")
print("Number of attempts:",attempt)