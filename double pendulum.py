import pygame
from math import sin, cos, pi

height, width = 600, 600
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((height, width))
pygame.display.set_caption('DOUBLE PENDULUM SIMULATION!')
gravity = .918
running = True


class Pendulum(object):
    def __init__(self, mass1, radius1, mass2, radius2, gravity, c1, c2, x=width / 2, y=height / 4):
        self.default_x, self.default_y = x, y
        self.mass1 = mass1
        self.mass2 = mass2
        self.radius1 = radius1
        self.radius2 = radius2
        self.theta1 = pi / 2
        self.theta2 = pi / 4
        self.acceleration1 = 0
        self.acceleration2 = 0
        self.velocity1 = 0
        self.velocity2 = 0
        self.gravity = gravity
        self.force1 = 0
        self.force2 = 0
        self.c1 = c1
        self.c2 = c2

    def simulate(self):
        self.update_vector()
        x1 = self.radius1 * sin(self.theta1) + self.default_x
        y1 = self.radius1 * cos(self.theta1) + self.default_y
        x2, y2 = self.radius2 * sin(self.theta2) + x1, self.radius2 * cos(self.theta2) + y1
        self.draw(x1, y1, x2, y2)
        pygame.display.update()

    def draw(self, pendulum1_x, pendulum1_y, pendulum2_x, pendulum2_y):
        pygame.draw.line(window, self.c1, [self.default_x, self.default_y], [pendulum1_x, pendulum1_y], width=2)
        pygame.draw.circle(window, self.c1, [pendulum1_x, pendulum1_y], self.mass1)
        pygame.draw.line(window, self.c2, [pendulum1_x, pendulum1_y], [pendulum2_x, pendulum2_y], width=2)
        pygame.draw.circle(window, self.c2, [pendulum2_x, pendulum2_y], self.mass2)

    def update_vector(self):
        self.acceleration1 = self.get_acceleration_value_theta1()
        self.velocity1 += self.acceleration1
        self.theta1 += self.velocity1

        self.acceleration2 = self.get_acceleration_value_theta2()  # + self.acceleration1
        self.velocity2 += self.acceleration2
        self.theta2 += self.velocity2

    def get_acceleration_value_theta1(self):
        n1 = -(self.gravity * ((2 * self.mass1) + self.mass2) * sin(self.theta1))
        n2 = -(self.mass2 * self.gravity * sin(self.theta1 - (2 * self.theta2)))
        n3 = 2 * sin(self.theta1 - self.theta2) * self.mass2
        n4 = (((self.velocity2 ** 2) * self.radius2) + ((self.velocity1 ** 2) * self.radius1 * cos(
            self.theta1 - self.theta2)))
        d1 = self.radius1 * (2 * self.mass1 + self.mass2 - (self.mass2 * cos((2 * self.theta1) - (2 * self.theta2))))
        return (n1 + n2 - (n3 * n4)) / d1

    def get_acceleration_value_theta2(self):
        n1 = 2 * sin(self.theta1 - self.theta2)
        n2 = ((self.velocity1 ** 2) * self.radius1 * (self.mass1 + self.mass2))
        n3 = self.gravity * (self.mass1 + self.mass2) * cos(self.theta1)
        n4 = (self.velocity2 ** 2) * self.radius2 * self.mass2 * cos(self.theta1 - self.theta2)
        d1 = self.radius2 * ((2 * self.mass1) + self.mass2 - (self.mass2 * cos((2 * self.theta1) - (2 * self.theta2))))
        return (n1 * (n2 + n3 + n4)) / d1


pendulum_obj1 = Pendulum(20, 200, 20, 150, gravity, (3, 244, 252), (252, 3, 231))
pendulum_obj2 = Pendulum(20, 200, 30, 150, gravity, (252, 136, 3), (252, 136, 3), 260, 80)


def play():
    global running
    while running:
        window.fill((0, 0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pendulum_obj1.simulate()
        pendulum_obj2.simulate()
    pygame.display.update()


play()
