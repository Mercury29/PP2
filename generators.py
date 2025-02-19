f=int(input("How much squares should i write?: "))
class MyNumbers:  #Task 1
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return (x**2)

myclass = MyNumbers()
myiter = iter(myclass)

for i in range(f):
  print(next(myiter))

j = int(input("How much even numbers?: "))
class MyNumbers:  #Task 2
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return (x*2)

myclass = MyNumbers()
myiter = iter(myclass)

for i in range(j):
  print(next(myiter))

g=int(input("How much numbers should i write?: "))
class MyNumbers:  #Task 3
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return (x*12)

myclass = MyNumbers()
myiter = iter(myclass)

for i in range(g):
  print(next(myiter))


i = int(input("Enter a 1st number: "))
o = int(input("Enter a 2nd number: "))
p = o - i
class MyNumbers:  #Task 4
  def __iter__(self):
    self.a = i
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return (x**2)

myclass = MyNumbers()
myiter = iter(myclass)
for i in range(p):
    print(next(myiter))

h = int(input("Enter a number: "))
class MyNumbers:  #Task 5
  def __iter__(self):
    self.a = h
    return self

  def __next__(self):
    x = self.a
    self.a -= 1
    return (x)

myclass = MyNumbers()
myiter = iter(myclass)

for i in range(h):
  print(next(myiter))