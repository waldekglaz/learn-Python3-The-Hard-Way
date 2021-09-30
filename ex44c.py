class Parent(object):
    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTRE PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()
