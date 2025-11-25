string=input("Enter a String:")
count=0
vowels=['a','e','i','o','u']
for i in string:
    if i in vowels:
        count+=1
        print(i)
print("vowels in string:",count)
