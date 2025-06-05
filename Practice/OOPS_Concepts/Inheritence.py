#SINGLE INHERITANCE

class A:
    def state1(self):
        print("Class A: State 1")
    def state2(self) :
        print("Class A: State 2")

class B(A):  #Classing Class A to ClassB
    def state3(self):
        print("Class B: State 3")
    def state4(self):
        print("Class B: State 4")

c= B()
#After calling A class in Class B we can see Class A methods in Class B
# c.state1()
# c.state4()

#MULTI LEVEL INHERITANCE

class AA:
    def state1(self):
        print("Class AA: State 1")
    def state2(self) :
        print("Class AA: State 2")

class BB(AA):  #Classing Class A to ClassB
    def state3(self):
        print("Class BB: State 3")
    def state4(self):
        print("Class BB: State 4")

class CC(BB): #Classing Class BB to Class CC , So that we can call AA and BB methods to Class CC
    def state5(self):
        print("Class CC: State 5")
    def state6(self):
        print("Class CC: State 6")

c= CC()
# c.state1()
# c.state2()
# c.state3()

#MUTLTILEVEL INHERITANCE:
class AA:
    def state1(self):
        print("Class AA: State 1")
    def state2(self) :
        print("Class AA: State 2")

class BB():  #Classing Class A to ClassB
    def state3(self):
        print("Class BB: State 3")
    def state4(self):
        print("Class BB: State 4")

class CC(AA,BB): #Classing Class BB,AA to Class CC is called Multilevel Inheritence
    def state5(self):
        print("Class CC: State 5")
    def state6(self):
        print("Class CC: State 6")

o=CC()
c.state1()
c.state2()
c.state3()

