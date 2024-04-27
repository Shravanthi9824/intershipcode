class A:
    def _init_(self):
        self.b=self.B()
    class B:
        def _init_(self):
            self.c=self.C()
        def fun(self):
            print("fun run")
        class C:
            def _init_(self):
                print("C")
A()
