num = [2,3,5,4,6,8,9]
even = 0
odd = 0

for n in num:
    if n % 2 == 0:
        even +=1

    else:
        odd +=1

print("Even" , even)
print("Odd" , odd)