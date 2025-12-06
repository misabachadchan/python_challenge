available_items=["apple","soap","brush","banana"]
cart=[]

while True:
    item=input("Enter item:")
    if(item==available_items):
        item.append(cart)
    elif item=="exit":
        break
print(cart)



