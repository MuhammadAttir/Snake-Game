from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_segmemt()
        self.head=self.segments[0]
        
    def create_segmemt(self):
        for position in STARTING_POSITIONS:
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for seg_no in range(len(self.segments)-1,0,-1):
            x=self.segments[seg_no-1].xcor()
            y=self.segments[seg_no-1].ycor()
            self.segments[seg_no].goto(x,y)
        self.head.forward(DISTANCE)
            
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
            
    def add_segment(self):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        
        last_segment_x=self.segments[-1].xcor()
        last_segment_y=self.segments[-1].ycor()
        
        new_segment.goto(last_segment_x,last_segment_y)
        self.segments.append(new_segment)