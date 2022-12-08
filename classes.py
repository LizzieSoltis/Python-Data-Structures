#Python Object-Oriented Programming
#Part 1/2 on Classes: Covers Class Instances and Instance Variables 
'''
Why Classes?
-Classses allow us to logically group our data and functions in a way that's easy to reuse and also easy to build upon if need be
-Data and functions mentioned are called class attributes and methods
'''

#EX 
'''
Say we had an appliction to our company
and we we wanted to represent our employees in our python code
-Use of a class will be great for this because each employee will have specific attributes and methods like name, email, pay, and actions they can perform
-So we can create a blueprint for employees
'''

class Employee:
    pass #can put this if you wanna leave error code for a sec

    #a class is a blueprint for creating instances
    #so, each unique employee will be an instance of that class

emp_1 = Employee() #instance 1 of that class
emp_2 = Employee() #instance 2 of that class

#each employee is a unique instance of that class
print("\nPart 1") #ignore these, meant for breaking out terminal output

print(emp_1) 
print(emp_2)
#it prints __main__.Employee object (meaning same class object) BUT at different 0x0000000 <- it's unique point in memory

'''
Instance variables that contains data that is unique to each instance
- .first, .last, .email, .pay are instance variable
- Notice how at this point, Employee() doesn't have an __init__ assigning these, 
but they can still be assigned/created and printed
'''
emp_1.first = "Corey" 
emp_1.last = "Shafer"
emp_1.email = "Corey.Schafer@gmail.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@gmail.com"
emp_2.pay = 60000

print("\nPart 2")

print(emp_1.email)
print(emp_2.email)

'''
Essentially the above^^ is doing the action of __init__ method in a class
-So, doing it manually would be a good starting point if your unsure of what a classes' instance variables should be, see what attributes are repeated the most and those should be the variables
-Doing it manually is not beneficial for the finished code as coding it is prone to mistakes, which is why we use classes
'''

#Employee1() is same as Employee() just moving on with new content

class Employee1():
    def __init__(self, first, last, pay): #this is the constructor of the class
        #classes recieve the instance as the first argument automatically
        #And so by convention, we call the instance self now (you can call it whatever but you should stick with self)
        #After self, we can choose any other arguments you can the class to accept

        #Now we set all of these instance variables
        self.first = first #this is the same thing as above when saying emp_1.first = "Corey", now its just automatically set
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"


#now when we call an instance of this class, we can pass in the values we specified in __init__
newEmp1 = Employee1("Corey", "Shafer", 50000)
newEmp2 = Employee1("Test","User",60000)

print("\nPart 3")

print(newEmp1.email)
print(newEmp2.email)

'''
To perform some kind of action, we can add methods to our class
EX
Lets say you wanted the ability to display the full name of an employee
'''
print("\nPart 4")
#Manual way to do it:
print("{} {}".format(newEmp2.first,newEmp2.last))

#Better way to do it:
class Employee2: #same as other employee classes, just moving on with content
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self): #remember each method of a class automatically takes in the instance of the class, called self
        #if self is not given, when you go to run this method on an instance of this class, an error will be thrown saying fullname() accepts 0 arguments but 1 was given (the 1 arg being the instance)
        #for this method we need the employees first and last name so the only argument we need passed in is the instance, self because that gives us the first and last name
        return "{} {}".format(self.first,self.last) 
            #this return uses the same logic as when we did it manually,
            #but it uses self.first and self.last insted of newEmp2.first&last so that it works for all instances

newEmpp1 = Employee2("Corey", "Schafer", 50000)
newEmpp2 = Employee2("Test", "User", 60000)

print(newEmpp2.fullname()) #parenthesis for fullname() is because it is a method not attiribute
#print(newEmpp2.fullname) ----> if () left off, it prints the method and not the return value of that method

'''
Now we have full advantage of code reuse 
- We can use the methods to do its actions for different instances which is easier and is less code than doing it manually
'''
print(newEmpp1.fullname())
newEmpp3 = Employee2("Classes make tasks", "so much easier", 1000)
print(newEmpp3.fullname())

'''
We can also run these methods using the class name, which makes it a bit more obvious of what's going on in the background
'''
print("\nPart 5")
#EX: 
newEmpp3 = Employee2("Classes make tasks", "so much easier", 1000)
#What we did before:
print(newEmpp3.fullname())
#What we do to run the methods using the class name
Employee2.fullname(newEmpp3) 

#Both lines do the exact same thing BUT: 
    #newEmpp3.fullname() is a method call on an instance of a class, which is passed through as self
    #Employee2.fullname(newEmpp3) is a method call on a class that then passes in the specific class instance that we want the method to act on
#So, they do the same exact thing, the second line just shows exactly what's going on in the background



