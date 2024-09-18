class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name}, Year of Birth: {self.yob}"

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student - {super().describe()}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher - {super().describe()}, Subject: {self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor - {super().describe()}, Specialist: {self.specialist}"

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)
    
    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))
    
    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        return sum(teacher.yob for teacher in teachers) / len(teachers)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            print(person.describe())
            
# ----------------------------------------------------------------------------------

ward = Ward("Downtown")
ward.add_person(Student("Alice", 2005, "10th"))
ward.add_person(Teacher("Mr. John", 1980, "Math"))
ward.add_person(Teacher("Ms. Sarah", 1975, "Physics"))
ward.add_person(Doctor("Dr. Smith", 1970, "Cardiology"))
ward.add_person(Doctor("Dr. Emily", 1985, "Neurology"))

print("Number of Doctors:", ward.count_doctor())

ward.sort_age()

print("Average Year of Birth of Teachers:", ward.compute_average())

ward.describe()