
#python classes and objects
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

#python dunder(magic) methods
# declare our own string class
class String:
	
	# magic method to initiate object
	def __init__(self, string):
		self.string = string
		
	# print our string object
	def __repr__(self):
		return 'Object: {}'.format(self.string)

# Driver Code
if __name__ == '__main__':
	
	# object creation
	string1 = String('Hello')

	# print object location
	print(string1)
