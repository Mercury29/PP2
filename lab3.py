#'''Function 1'''
#'''Questuion1'''
#def t(a):
#
#    ounces=(28.3495231*a)
#    print(round(ounces,7))
#gramms=int(input())
#t(gramms)
#
#'''Questuion2'''
#def t(a):
#    C=(5/9)*(a-32)
#    print(C)
#F=int(input())
#t(F)
#'''Questuion3'''
#def prime(n):
#    if n < 2:  
#        return False
#    for i in range(2, int(n**0.5) + 1): 
#        if n % i == 0:
#            return False
#    return True
#def filter_prime(numbers):
#    return [num for num in numbers if prime(num)]
#numbers = list(map(int, input().split()))
#print(filter_prime(numbers))
#'''Questuion4'''
#import itertools
#def per():
#    s=input()
#    p=itertools.permutations(s)
#    for pe in p:
#        print("".join(pe))
#per()
#'''Questuion5'''
#import itertools
#def p():
#    a=input()
#    q=itertools.permutations(a)
#    for i in q:
#        print("".join(i))
#p()
#'''Questuion6'''
#def t():
#    a=input()
#    a=a.split()
#    print(" ".join(a[::-1]))
#t()
#'''Questuion7'''
#def t(a):
#    for i in range(m-1):
#        if((a[i]==3) and (a[i+1]==3)):
#            return True
#    return False
#m=int(input())
#a=[0]*m
#for i in range(m):
#    a[i]=int(input())
#print(a,"->" ,t(a))
#'''Questuion8'''
#def t(a):
#    for i in range(m-2):
#        if((a[i]==0) and (a[i+1]==0)and (a[i+2]==7)):
#            return True
#    return False
#m=int(input())
#a=[0]*m
#for i in range(m):
#    a[i]=int(input())
#print(a,"->" ,t(a))
#'''Questuion9'''
#def r(a):
#    a=4*(a**3)/3
#    print(a,"PI")
#b=int(input())
#r(b)
#'''Questuion10'''
#def t(a):
#    
#    for i in b:
#        if i not in a:
#            a.append(i)
#    return a
#m=int(input())
#a=[0]*m
#b=[0]*m
#for i in range(m):
#    a[i]=input()
#for i in range(m):
#    b[i]=input()
#print(t(a))
#'''Questuion11'''
#def palindrome(word):
#    return word == word[::-1]
#print(palindrome('radar'))
#
#
#'''Questuion12'''
#def histogram(numbers):
#    for num in numbers:
#        print('*' * num)
#
#histogram([4, 9, 7])
#'''Questuion13'''
#import random
#
#def guess_the_number():
#    print("Hello! What is your name?")
#    name = input()
#
#    number_to_guess = random.randint(1, 20)
#    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
#
#    attempts = 0
#    while True:
#        print("Take a guess.")
#        try:
#            guess = int(input())
#        except ValueError:
#            print("Please enter a valid number.")
#            continue
#
#        attempts += 1
#
#        if guess < number_to_guess:
#            print("Your guess is too low.")
#        elif guess > number_to_guess:
#            print("Your guess is too high.")
#        else:
#            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
#            break
#
#    guess_the_number()
#
#'''Function 2'''
#
#movies = [
#{
#"name": "Usual Suspects", 
#"imdb": 7.0,
#"category": "Thriller"
#},
#{
#"name": "Hitman",
#"imdb": 6.3,
#"category": "Action"
#},
#{
#"name": "Dark Knight",
#"imdb": 9.0,
#"category": "Adventure"
#},
#{
#"name": "The Help",
#"imdb": 8.0,
#"category": "Drama"
#},
#{
#"name": "The Choice",
#"imdb": 6.2,
#"category": "Romance"
#},
#{
#"name": "Colonia",
#"imdb": 7.4,
#"category": "Romance"
#},
#{
#"name": "Love",
#"imdb": 6.0,
#"category": "Romance"
#},
#{
#"name": "Bride Wars",
#"imdb": 5.4,
#"category": "Romance"
#},
#{
#"name": "AlphaJet",
#"imdb": 3.2,
#"category": "War"
#},
#{
#"name": "Ringing Crime",
#"imdb": 4.0,
#"category": "Crime"
#},
#{
#"name": "Joking muck",
#"imdb": 7.2,
#"category": "Comedy"
#},
#{
#"name": "What is the name",
#"imdb": 9.2,
#"category": "Suspense"
#},
#{
#"name": "Detective",
#"imdb": 7.0,
#"category": "Suspense"
#},
#{
#"name": "Exam",
#"imdb": 4.2,
#"category": "Thriller"
#},
#{
#"name": "We Two",
#"imdb": 7.2,
#"category": "Romance"
#}
#]
#'''Q1'''
#def t(b):
#    for i in movies:
#        if(b==i["name"]):
#            return i["imdb"]>5.5
#    return False
#a=input()
#print(t(a))
#
#'''Q2'''
#def high(a):
#    return[i for i in a if i["imdb"]>5.5]
#n=high(movies)
#for i in n:
#    print(i)
#
#'''Q3'''
#def t(b):
#    return[i for i in movies if i["category"]==b]
#a=input()
#n=t(a)
#for i in n:
#    print(i)
#
#'''Q4'''
#
#def t():
#    b=0
#    a=0
#    for i in movies:
#        b+=i["imdb"]
#        a+=1
#    b=b/a
#    print(b)
#t()
#
#'''Q5'''
#
#def t(b):
#    return[i for i in movies if i["category"]==b and i["imdb"]>5.5]
#a=input()
#n=t(a)
#o=0
#for i in n:
#    o+=i["imdb"]
#print(o)

'''Classes'''
# Task 1
class A:
    def __init__(self):
        self.a = ""
    
    def b(self):
        self.a = input("Enter a string: ")
    
    def c(self):
        print(self.a.upper())

# Task 2
class D:
    def e(self):
        return 0

class F(D):
    def __init__(self, a):
        self.a = a
    
    def e(self):
        return self.a ** 2

# Task 3
class G(D):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def e(self):
        return self.a * self.b

# Task 4
import math
class H:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def i(self):
        print(f"Point({self.a}, {self.b})")
    
    def j(self, c, d):
        self.a = c
        self.b = d
    
    def k(self, l):
        return math.sqrt((self.a - l.a) ** 2 + (self.b - l.b) ** 2)

# Task 5
class M:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b
    
    def n(self, c):
        self.b += c
        print(f"Deposited {c}. New balance: {self.b}")
    
    def o(self, c):
        if c > self.b:
            print("Insufficient funds!")
        else:
            self.b -= c
            print(f"Withdrawn {c}. New balance: {self.b}")

# Task 6
p = list(range(1, 21))
q = lambda a: a > 1 and all(a % b != 0 for b in range(2, int(math.sqrt(a)) + 1))
r = list(filter(q, p))
print("Prime numbers:", r)
