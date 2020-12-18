
"""
The program will take the students grades from the Final.txt and count how many 
grades are in the file. Next it will return to the user how many grades there where.
It will then add up all the grades and divide by the number of grades 
there were to determine the class grade average and return that number to the user.
Lastly, it will calculate the percentage of grades that are above the class average
and return that number to the user.
"""

"""
infile = open final.txt
grades = the grades in a line
infile close()
for i in range lens grades
    grades = int

for grades
    if > average

print numbe of grades
print average grade
print grades above average
"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
print("Total Grades are:", len(grades))
print("The Average of the Grades is:", average)
print("The Percentage of Grades that are above the average is: {0:.2f}%".format(100 * num / len(grades)))