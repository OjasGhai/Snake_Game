from turtle import Turtle, Screen
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
class Snake:
    def __init__(self):
        self.turtles = []
        self.createsnake()
        self.head = self.turtles[0]

    def createsnake(self):
        for position in starting_positions:
            self.add_snake(position)

    def add_snake(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color("yellow")
        tim.speed("fastest")
        tim.goto(position)
        self.turtles.append(tim)

    def extend_snake(self):
        self.add_snake(self.turtles[-1].position())



    def move(self):
        for turtle_no in range(len(self.turtles) - 1, 0, -1):
            nex_x = self.turtles[turtle_no - 1].xcor()
            new_y = self.turtles[turtle_no - 1].ycor()
            self.turtles[turtle_no].goto(nex_x, new_y)
        self.turtles[0].forward(MOVE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            return
        pass
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            return
        pass

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)



