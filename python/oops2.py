class Employee:
    def print_details(self):
        return f"Name is {self.name}, section is {self.section}, roll number is {self.roll_number}"


rohan = Employee()
rohan.name = "Ajit"
rohan.section = 1
rohan.roll_number = 15
print(rohan.print_details())
