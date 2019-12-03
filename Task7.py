class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def info(self):
        return (self.name , self.age , self.major)
        
        


Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve.info())
# <name: Steven Schultz, age: 23, major: English>
print(Johnny.info())
# <name: Jonathan Rosenberg, age: 24, major: Biology>