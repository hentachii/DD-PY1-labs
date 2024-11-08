numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a1 = sum(numbers[00:4])
a2 = sum(numbers[5:])
a3 = a1 + a2
b1 = len(numbers)
c1 = a3 / b1
numbers[4]= c1
print("Измененный список:", numbers )
