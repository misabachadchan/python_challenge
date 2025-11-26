def sum_var_args(numbers):
    return sum(numbers)

n = int(input("How many numbers? "))
lst = [int(input("Enter number: ")) for _ in range(n)]
print("Sum:", sum_var_args(lst))
