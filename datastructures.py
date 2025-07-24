# Creating a list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)
# Output: [1, 2, 3, 4, 5]
numbers.extend( [5, 6, 7, 8])
print(numbers)
numbers.pop()
print(numbers)
print("The sixth element is:", numbers[5])
numbers[1] = 9
print("the modified list is:", numbers)

numbersa = [1, 2, 3, 4]
numbersb = [5, 6, 7, 8]
numbersa.extend(numbersb)
print ("numbers a")
numbersa.pop()
print(numbersa)
print("The first element is:", numbersa[0])
numbersa [4]= 8
print(numbersa)
numbersc = [5, 7, 9]
numbersa.extend(numbersc)
print(numbersa)
numbersa.remove(7)
print(numbersa)
