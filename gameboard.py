from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.center_line = []
        self.center()

    def center(self):
        for i in range(20):
            dash_unit = Turtle()
            dash_unit.penup()
            dash_unit.shape("square")
            dash_unit.color("white")
            dash_unit.speed("fastest")
            dash_unit.shapesize(stretch_len=0.1, stretch_wid=0.4)
            dash_unit.goto(0, 195 - 20*i)
            self.center_line.append(dash_unit)
