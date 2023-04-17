import sys

print(sys.version)
print(sys.executable)
print("Irtaza")


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Irtaza"))
