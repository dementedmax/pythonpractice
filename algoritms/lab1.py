from os import system

class Student:
    def __init__(self, surname, name, group, rates, next_student, prev_student):
        self.surname = surname
        self.name = name
        self.group = group
        self.rates = rates
        self.next_student = next_student
        self.prev_student = prev_student
    
    def get_data(self):
        data = "" + self.surname + " " + self.name + " " + self.group + " "
        for rate in self.rates:
            data = data + str(rate) + " "
        return data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

system('cls')
student = Student("Animovich","Anime","FIG-666",[1,1,1,5,5],0,0)
data = student.get_data()
print(data)