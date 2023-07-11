list = [1,2,3,4,5,6,7,8,9]
even_count, odd_count = 0, 0
for i in list:
    if i%2==0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers: ", even_count)
print("Number of odd numbers: ", odd_count)