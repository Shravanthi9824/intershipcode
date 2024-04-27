class A:
    def variable_declaration(self,amount):
        self.amount = amount
    def amount1(self):
         print(self.amount)
a=A()
b=A()
a.variable_declaration(1000)
b.variable_declaration(2000)
a.amount1()
b.amount1()
