# Write a program that gets input of student names, and each student will have 3 test scores.
# After all is entered, program will calculate averages and give a grade for each student.

import random

def userInput():
    students = []
    grades = []

    studentsNum = int(input("How many students are there? "))
    for x in range(studentsNum):
        studentsInput = input(f"Input name of student {x + 1}: ")
        students.append(studentsInput)
    
    gradesNum = 3
    for s in range(len(students)):
        gradesInputArray = []
        for g in range(gradesNum):
            gradesInput = round(float(input(f"Input grade {g + 1} for {students[s]}: ")), 2)
            gradesInputArray.append(gradesInput)
        grades.append(gradesInputArray)
    
    return(students, grades)

def arraySum(array):
    answer = 0
    for x in array:
        answer += x
    return answer

def gradeAvg(grades):
    # Duplicates grades array without overwriting the variable passed by reference
    answer = []
    for x in grades:
        answer.append(x)
    
    # Averages the input and assigns it to the duplicated array
    counter = 0
    for x in grades:
        answer[counter] = arraySum(x) / len(x)
        counter += 1
    return answer



def main():
    students, grades = userInput()
    avgGrades = gradeAvg(grades)

    # print(students)
    # print(grades)
    # print(avgGrades)

    counter = 0
    for s in students:
        print(f"{s}'s grade average is {round(avgGrades[counter], 2)}.")
        counter += 1

main()
