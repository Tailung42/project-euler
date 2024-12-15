LIMIT = 10
sum = 0
for num in range(LIMIT):
    if num % 3 == 0 or num % 5 == 0:
        sum += num
print(f"The sum is : {sum}")