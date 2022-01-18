class Real_Number :
    def __init__(self,real_number) :
        self.real_number = real_number
    def module(self) :
        return (self.real_number **2) ** 0.5

class Complex_Number(Real_Number) :
    def __init__(self,real_number, image_number) :
        super().__init__(real_number)
        self.image_number = image_number
    def module(self) :
        return (self.real_number**2 + self.image_number**2) ** 0.5

a = float(input("Real number input: "))
b = float(input("Image number input: "))
real = Real_Number(a)
comp = Complex_Number(a,b)
print("Module of Real Number: ",real.module())
print("Module of Complex Number: ",comp.module())