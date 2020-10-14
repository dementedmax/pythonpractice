from os import system
from random import choice, randint
import keyboard
from time import sleep

class Student:
    def __init__(self, surname, name, group, rates, next_student = None, prev_student = None):
        self.surname = surname
        self.name = name
        self.group = group
        self.rates = rates
        self.next_student = next_student
        self.prev_student = prev_student
    
    def getData(self):
        data = "" + self.surname + " " + self.name + " " + self.group + " "
        for rate in self.rates:
            data = data + str(rate) + " "
        return data

class SutudentsList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToEnd(self, newstudent):
        if self.head is None:
            self.head = newstudent
            self.tail = newstudent
            print("Add new student: " + newstudent.getData())
            return
        laststudent = self.head
        while (laststudent.next_student):
            laststudent = laststudent.next_student
        laststudent.next_student = newstudent
        newstudent.prev_student = laststudent
        self.tail = newstudent

        print("Add new student: " + newstudent.getData())

    def getStudents(self):
        lastStudent = self.head
        while (True):
            print(lastStudent.getData())
            lastStudent = lastStudent.next_student
            if(lastStudent == None):
                break

    def getStudentsRevers(self):
        lastStudent = self.tail
        while (True):
            print(lastStudent.getData())
            lastStudent = lastStudent.prev_student
            if(lastStudent == None):
                break

    def deleteStudentsByGroup(self, group):
        lastStudent = self.head
        while (True):
            if(lastStudent.group == group):
                lastStudent.prev_student.next_student = lastStudent.next_student
                lastStudent.next_student.prev_student = lastStudent.prev_student
            lastStudent = lastStudent.next_student
            if(lastStudent == None):
                break

surnames = ["Иванов", "Петров", "Петин", "Хохлов", "Ионов", "Чедов", "Макаров", "Казаков", "Оргеев", "Леммер"]
names = ["Иван", "Петр", "Максим", "Александр", "Владимир", "Николай", "Вадим", "Илья", "Денис", "Сергей"]
groups = ["ИВТ", "ПИН", "МО", "САУ", "ИСТ"]

student_list = SutudentsList()

for i in range(20):
    student_list.addToEnd(Student(
        surname = choice(surnames),
        name = choice(names),
        group = choice(groups),
        rates = [randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5)]
        ))

print("Список студентов в прямом порядке: ")
student_list.getStudents()
print("\n")
print("Список студентов в обратном порядке: ")
student_list.getStudentsRevers()
print("\n")

deleted_group = choice(groups)
print("Удаляем студентов группы " + deleted_group + " и выводим в прямом порядке: ")
student_list.deleteStudentsByGroup(deleted_group)
student_list.getStudents()
print("\n")
print("Выводим список без удалённых студентов в обратном порядке: ")
student_list.getStudentsRevers()