import turtle
import random as rnd

#setup
tiltRange = 30
sproutRange = 45
depth = 10
logLen = 50
width = 1.25

class Branch:
    
    def __init__(self, depth, angle) -> None:
        self.depth = depth
        self.pen = turtle.Turtle()
        self.angle = 90 if angle == None else angle
        self.tilt = (rnd.random() * 2 - 1) * tiltRange

        self.pen.speed(0)
        
    def FirstBranch(self):
        self.pen.penup()
        self.pen.goto(0, -200)
        self.pen.pendown()

    def Draw(self):
        #reset the heading for precise angle
        self.pen.setheading(self.angle)

        #slowing bending branch more natural look
        n = 10
        for i in range(n):
            #slowly decrease depth linearly
            imDepth = (self.depth - (1 / n) * (i - 1))

            self.pen.pensize(imDepth * width)
            self.pen.right((self.tilt * (imDepth / depth)) / n)
            self.pen.forward((logLen * ((self.depth + 1) / (depth + 1))) / n)

        self.angle = self.pen.heading()
        self.depth -= 1

    def Sprout(self):
        angle = self.angle + (rnd.random() * 2 - 1) * sproutRange
        branch = Branch(self.depth - 1, angle)
        self.angle += self.angle - angle

        branch.pen.penup()
        branch.pen.goto(self.pen.pos())
        branch.pen.pendown()

        return branch


def Grow(branchs : list[Branch]):

    openBranchs = branchs
    while (openBranchs):
        for branch in openBranchs:
            """
            3 steps
            1 : If end hide then end branch
            2 : extend branch
            3 : chance to spawn more branch
            """

            if branch.depth <= 0:
                branch.pen.hideturtle()
                continue

            branch.Draw()

            if (rnd.random() > 0):
                openBranchs.append(branch.Sprout())

            openBranchs.append(branch)


if __name__ == '__main__':
    branchs = []

    branchs.append(Branch(depth, 90))

    branchs[0].FirstBranch()

    Grow(branchs)

    turtle.exitonclick()