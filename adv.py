class A:
    def feature1(self):
        print("its working fine")
    def feature2(self):
        print("its working better then fine")
class B:
    def feature3(self):
        print("its working next level")
    def feature4(self):
        print("reached the level")
class C(A,B):
    def feature5(self):
        print("reached the great level")

a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature4()
b1.feature3()
c1 = C()
c1.feature4()
c1.feature3()
c1.feature2()
c1.feature1()
c1.feature5()
