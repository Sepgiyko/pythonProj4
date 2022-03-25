class Student:
    __age = 0

    def setAge(self, age):
        if age > 0:
            self.__age = age

    def getAge(self):
        return self.__age

student = Student()

student.setAge(15)
print(student.getAge())

student.setAge(-3)
print(student.getAge())

student.setAge(21)
print(student.getAge())
