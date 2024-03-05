class Employee:
    def putdata(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter their salary: "))

    def display(self):
        print("Name is: ", self.name)
        print("Age is: ", self.age)
        print("Salary is: ", self.salary)


a = Employee()
a.putdata()
a.display()
