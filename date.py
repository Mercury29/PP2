import datetime

x = datetime.datetime.now() #1st task
w = x
x = int(x.strftime("%d"))-5
print("first task: ", x, "th day of this month was 5 days ago")

q = w.strftime("%w") #2nd task
if q == "0":
    print("Today is Sunday")
    print("Yesterday was Saturday")
    print("Tomorrow is Monday")
elif q == "1":
    print("Today is Monday")
    print("Yesterday was Sunday")
    print("Tomorrow is Tuesday")
elif q == "2":
    print("Today is Tuesday")
    print("Yesterday was Monday")
    print("Tomorrow is Wednesday")
elif q == "3":
    print("Today is Wednesday")
    print("Yesterday was Tuesday")
    print("Tomorrow is Thursday")
elif q == "4":
    print("Today is Thursday")
    print("Yesterday was Wednesday")
    print("Tomorrow is Friday")
elif q == "5":
    print("Today is Friday")
    print("Yesterday was Thursday")
    print("Tomorrow is Saturday")
elif q == "6":
    print("Today is Saturday")
    print("Yesterday was Friday")
    print("Tomorrow is Sunday")

y=datetime.datetime.now() #3nd task
print(y.strftime("%c"))


