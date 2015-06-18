
!bc pyoptpro
class Line:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, x):
        a, b = self.a, self.b
        return a*x + b

line = Line(2, 1)
y = line(x=3)
print y
!ec

