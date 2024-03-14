def hello():
    print("Hello! My name is Somchai.")

# hello()
def helloName(name):
    print("Hello! My name is " + name)

# helloName("Somsak")
# helloName("Somsri")
# helloName("Sompong")
def helloNameAge(name, age):
    print(f"Hello! My name is {name}")
    print(f"I am {age} years old.")

# helloNameAge("Somchai", 50)
# helloNameAge(name="Somchai", age=50)
# helloNameAge(age=80, name="Somying")

# Optional Parameter
def helloOptional(name, age=60):
    print(f"Hello! My name is {name}")
    print(f"I am {age} years old.")

# helloOptional("Somsak")
# helloOptional("Somying", 30)

def addNumber(x, y):
    return x + y

# sum = addNumber(10, 20)
def calculate(z):
    return addNumber(10, 20) * z

result = calculate(5)
print(result)