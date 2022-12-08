#Python Object-Oriented Programming
#Part 2/2 on Classes: Covers Class Variables
'''
Class Variables are variables that are shared among all instances of a class
- So while instance variables can be unique for each instance, like each employee's name and email, class variables should be the same for each instance
    - When building a class, you want to look at what types of data you want to be shared among all instances of an object
    - i.e. if class for cars, all cars have four wheels no matter what, so it'd be a good class variable; self.wheels = 4
'''
#For our example of employees, lets say our coupany gives annual raises every year. 
#The amount can change from year to year but whatever that amount is, it will be the same for all employees.
#This is a good canidate to be a class variable
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp1 = Employee("Corey", "Shafer", 50000)
emp2 = Employee("Test","User",60000)

print("\nPart 1") #Ignore these, meant for breaking up terminal output

#You could create a method to give the raise to each employee, like the apply_raise() method defined above^:
#And then do: 
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay) #---> emp1 raise would be now 52000 instead of 50000, so this works
#BUT:
    #It would be nice to access the raise amount by doing something like emp_1.raise_amount
    #raise_amount attribute currently doesn't exist, so we can't see that it's 4%
    #Also, if we wanted to easily update the raise amount of 4% to be something different, we currently couldn't because it's hidden within the apply_raise() method

'''
So, if there's an attribute of a class that you wouldn't want to go into the code manually to change/update the value, its best to make it a class variable
- i.e we want to be able to change the raise amount, so we will put it in the __init__ method of the class
'''

print("\nPart 2")

class Employee1: #Same idea as Employee(), just moving on with content

    raise_amount = 1.04 #class variable has been made

    def __init__(self, first, last, pay):
        self.first = first #these are attributes that an instance would contain
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #self.raise_amount is called to pull raise_amount attribute from self (instance of Employee1())

emp_1 = Employee1("Corey", "Shafer", 50000)
emp_2 = Employee1("Test","User",60000)
print("\nGetting raise amount for employee class")
print(Employee1.raise_amount) #amount is 1.04
print(emp_1.raise_amount) #amount is the same
print(emp_2.raise_amount) #amount is the same

print("\nChanging raise amount for employee class")
Employee1.raise_amount = 2.04 #raise_amount for employee class (so for all instances of that class) is now changed to 2.04
print(Employee1.raise_amount) #amount is 2.04
print(emp_1.raise_amount) #amount is the same
print(emp_2.raise_amount) #amount is the same

print("\nChanging raise amount for specific instance of employee class")
emp_1.raise_amount = 3.04 #raise_amount for JUST the emp_1 instance of employee class is 3.04
print(Employee1.raise_amount) #raise_amount for employee class is still 2.04
print(emp_1.raise_amount) #amount is 3.04
print(emp_2.raise_amount) #amount is 2.04

'''
What is going on above is that when we try to access an attribute on an instance, it will:
    1. First check if the instance contains that attribute, and if it doesnt, then
    2. It will see if the class or any class that it inherits the instance from, contains the attribute
So when we access our raise amounts from our instances emp_1 and emp_2, the instances themselves don't actually have the raise_amount attribute;
    - The instances have the attributes of first and last name, pay, and email.
    - The class that inherits the instance from, Employee1(), has the attribute raise_amount
This shows how you can access and change class variables from the class itself and from the classes instances
- This is useful to know scope wise and if a class variable only needs to change for certain instances of that class
'''

#helpful tip if there's confusion when changing a class variable only for certain instances of that class:
#print(emp_1.__dict__) would output the data stored in all the class variables and instance attributes for that instance
#helps make sure you're changing what you want to because in a method like apply_raise(), it uses the class variable raise_amount to change the employees pay
#so, you'd get different results depending on whether you applied a class variable change on the instance(self), emp_1.raise_amount, or the employee class, Employee1.raise_amount

print("\nPart 3")

'''
Let's say you want a class variable where it wouldn't really make sense to use self
EX) If a company wanted to keep track of how many employeed that we have
- So, the number of employees should be the same for all instances of our class
- This is different than the raise_amount variable because this variable would be changed for specific employees (instances) or year to year,
the employee count would increment by 1 for a new employee instance and then be the same for all instances 
'''

class Employee2: #Same idea as Employee() and Employee1(), just moving on with content

    num_of_emps = 0 #class variable has been made
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee2.num_of_emps += 1 #since __init__ runs with every instance of the class, we can increment the amount of employees in this contructor method
        #Here we are using Employee2.num_of_emps instead of self.num_of_emps so that when it raises, the number of employees is constant and not different for any one instance
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

empp_1 = Employee2("Corey", "Shafer", 50000)
empp_2 = Employee2("Test","User",60000)
print(Employee2.num_of_emps) #returns 2, Employee2.num_of_emps was incremented twice
