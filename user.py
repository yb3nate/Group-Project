class User:
    #Within this class, different attributes are defined. 
    def __init__(self, name, major, courses, study_habits, availability):
        self.name =name
        self.major= major
        self.courses= courses
        self.study_habits =study_habits
        self.availability = availability

    def add_course(self, course):
        self.courses.append(course)
#This allows people to see the new students availability 
    def update_availability(self, new_availability):
        self.availability = new_availability
#Shows the ooverview of the studnets details on name, major, and courses
    def __str__(self):
        """Returns a string that represents the student's details."""
        return f"{self.name} - {self.major} - {', '.join(self.courses)}"