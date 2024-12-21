class Student:
    def __init__(self, id: int = 5, name: str = "John", age: int = 25, gpa: float = 3.45):
        if not isinstance(id, int):
            raise TypeError("iD can only be a integer")
        if not isinstance(name, str):
            raise TypeError("Name can only be a string")
        if not isinstance(age, int):
            raise TypeError("Age can only be a integer")
        if not isinstance(gpa, float):
            raise TypeError("GPA can only be an integer or number with 2 decimals")
        if gpa > 4:
            raise ValueError("You cannot have higher than a 4.0 GPA")
        self.id = id 
        self.name = name 
        self.age = age 
        self.gpa = gpa 


    def return_student_id(self):
        return self.id
    
    def return_student_name(self):
        return self.name
    
    def return_student_age(self):
        return self.age
    
    def return_student_gpa(self):
        return self.gpa
    
    def return_student_record(self):
        return "ID:" + str(self.id) + "\n" + \
                "Name:" + self.name + "\n " + \
                "Age:" + str(self.age) + "\n" + \
                "GPA:" + str(self.gpa)
