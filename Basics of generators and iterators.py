
#Python Iterators
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#python generators
def sq_numbers(n): 
	for i in range(1, n+1): 
		yield i*i 


a = sq_numbers(3) 

print("The square of numbers 1,2,3 are : ") 
print(next(a)) 
print(next(a)) 
print(next(a)) 
