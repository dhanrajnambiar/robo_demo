from django.db import models

# Create your models here.

class Robo(models.Model):
    dir_choices = [('NORTH','NORTH'),('EAST','EAST'),\
                    ('SOUTH','SOUTH'),('WEST','WEST')]
    name = models.CharField(max_length=100, unique=True)
    x_cordinate = models.IntegerField(default=0)
    y_cordinate = models.IntegerField(default=0)
    direction = models.CharField(choices=dir_choices, max_length=5)
    x_xtreme = 5
    y_xtreme = 5
    current_move_blocked = False
    right_rotate_dict = {
        "NORTH":"EAST",
        "EAST":"SOUTH",
        "SOUTH":"WEST",
        "WEST":"NORTH"
    }
    left_rotate_dict = {
        "NORTH":"WEST",
        "EAST": "NORTH",
        "SOUTH": "EAST",
        "WEST": "SOUTH"
    }

    def __str__(self):
        return self.name

    def report(self):
        return "Current Position is ({}, {}) facing {}"\
                .format(self.x_cordinate, self.y_cordinate, self.direction)

    def place(self, x_cord=0, y_cord=0, face="NORTH"):
        if 0 <= x_cord <= Robo.x_xtreme and 0<= y_cord <= Robo.y_xtreme:
            self.x_cordinate = x_cord
            self.y_cordinate = y_cord
            self.direction = face
            return {"status": "Success"}
        else:
            return {"status": "Failure"}

    def move(self):
        if self.direction == "NORTH" and \
            0 <= (self.y_cordinate + 1) <= Robo.y_xtreme:
            self.y_cordinate += 1
        elif self.direction == "EAST" and \
            0 <= (self.x_cordinate + 1) <= Robo.x_xtreme:
            self.x_cordinate += 1
        elif self.direction == "SOUTH" and \
            0 <= (self.y_cordinate - 1) <= Robo.y_xtreme:
            self.y_cordinate -= 1
        elif self.direction == "WEST" and \
            0 <= (self.x_cordinate - 1) <= Robo.x_xtreme:
            self.x_cordinate -= 1
        else:
            self.current_move_blocked = True
            return {"status": "Failure"}
        return {"status": "Success"}

    def right(self):
        self.direction = Robo.right_rotate_dict[self.direction]

    def left(self):
        self.direction = Robo.left_rotate_dict[self.direction]
