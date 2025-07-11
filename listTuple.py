L1 = [1,8,7,7,2,21,15]

third_item = L1.pop(2)
print(third_item)
print(1)

print(L1.remove(21))

# write a program to store 7 fruits in a list entered by the user.

fruits = []
for i in range(7):
    fruit = input("Enter a fruit name : ")
    fruits.append(fruit)

print(fruits)

# write a program to accept marks of 6 students and display in a sorted manner.
marks = []

for i in range(6):
    mark = int(input(f"Enter the marks of student {i+1} : "))
    marks.append(mark)

marks.sort()
print(marks)


# write a program to sum a list with 4 numbers

List = [1,2,3,4]
sum_of_list = sum(List)
print(sum_of_list)


