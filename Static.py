class Marks:
    def Math_num(a, b):
        return a + b

    def Sci_num(a, b):
        return a + b

    def Eng_num(a, b):
        return a + b


Marks.Math_num = staticmethod(Marks.Math_num)


print(" Total Marks in Maths", Marks.Math_num(64, 28))


Marks.Sci_num = staticmethod(Marks.Sci_num)


print(" Total Marks in Science", Marks.Sci_num(70, 25))


Marks.Eng_num = staticmethod(Marks.Eng_num)


print(" Total Marks in English", Marks.Eng_num(65, 30))
