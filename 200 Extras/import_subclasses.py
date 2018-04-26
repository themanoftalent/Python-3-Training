from subclass_exercise import *

dash = Pet("dash", "horse")
pongo = Dog("pongo", True)
furry = Cat("furry", True)

print( "Horse: %s" % dash)
print( "Dog: %s" % pongo)
print( "Cat: %s" % furry)


print( "furry is an instance of Pet: %r" % isinstance(furry, Pet))
print( "furry is an instance of Cat: %r" % isinstance(furry, Cat))
print( "pongo is an instance of Pet: %r" % isinstance(pongo, Pet))
print( "dash is an instance of Pet: %r" % isinstance(dash, Pet))
print( "pongo is an instance of Cat: %r" % isinstance(pongo, Cat))
print( "dash is an instance of Dog: %r" % isinstance(dash, Dog))
