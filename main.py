total = 0
for number in range(1, 101): 
    if number % 2 == 0: 
        total+= number
print(f"The total of all even numbers from 1 to 100 is {total}")