class Person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay


bob = Person('Bob Smith')
sue = Person('Sue Jones',job='dev',pay=10000)
print(bob.name,bob.pay)
print(sue.name,sue.pay)
print(bob.name.split()[-1])