'''def add_number(x,y):
    return x+y;

x=(int(input("Enter first number")))
y=(int(input("Enter second number")))

print("sum =", add_number(x, y))'''


def add():
    a = 10
    b = 40
    print(a + b)

def sub():
    a = 10
    b = 40
    print(a - b)

def multi():
    a = 10
    b = 40
    print(a * b)

def div():
    a = 10
    b = 40
    print(a / b)

print("1 - Add")
print("2 - Sub")
print("3 - Multi")
print("4 - Div")
print("5 - Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    add()
elif choice == 2:
    sub()
elif choice == 3:
    multi()
elif choice == 4:
    div()
else:
    print("Good Bye!")
flag=input("Do you want to continu(y/n)")
print(flag)
if(flag=="n"):
  print("Thank you")