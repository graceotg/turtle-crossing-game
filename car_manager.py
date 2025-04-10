from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

ending_of_chance = 6



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, ending_of_chance)   # ending of chance can be changed to make game harder
        if random_chance == 1:  # this ensures that there is space between when each car is created
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=0.8, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)


    def move(self):
        for car in self.car_list:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        global ending_of_chance
        ending_of_chance = 5



