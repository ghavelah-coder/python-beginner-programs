marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Total marks:", sum(marks))
print("Average marks:", average)
