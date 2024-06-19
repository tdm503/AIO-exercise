class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        print(f"Name : {self.name} - YoB : {self.yob}", end="")


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print("Student - ", end="")
        super().describe()
        print(f" - Grade : {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print("Teacher - ", end="")
        super().describe()
        print(f" - subject : {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print("Doctor - ", end="")
        super().describe()
        print(f" - specialist : {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        total_years = sum(teacher.yob for teacher in teachers)
        return total_years / len(teachers)


# 2a
student1 = Student(name="StudentA", yob=2010, grade='7')
student1.describe()
doctor1 = Doctor(name="abc", yob=2000, specialist="y ta")
doctor1.describe()
teacher1 = Teacher(name="def", yob=1999, subject="math")
teacher1.describe()
# 2b
print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="his")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.describe()

# 2c
print(f'\nNumber of doctors : {ward1.count_doctor()}')

# 2d
print('\nAfter sorting Age of ward1 people')
ward1.sort_age()
ward1.describe()

# 2e
print(f"\nAverage year of birth (teacher) : {ward1.compute_average()}")
