class Robot:
    # A class variable, counting the number of robots
    population = 0
    def __init__(self, name):
        #   Initializes the data
        self.name = name
        print("Making {0}".format(self.name))
        # When this robot is made, the robot
        # population increases by 1
        Robot.population += 1
    def die(self):
    # Destroy robot
        print("{0} is being destroyed".format(self.name))
        Robot.population -= 1
    def say_hi(self):
        print("Hello, my name is {0}.".format(self.name))
    # @classmethod
    def count_robots(self):
        # Prints the current population
        print("We have {0} robots.".format(Robot.population))

robot1 = Robot("Iron Man")
robot1.say_hi()
robot1.count_robots()
robot2 = Robot("Ultron")
robot2.say_hi()
robot2.count_robots()
print("\nRobots have finished their work. So let's destroy them.")
robot1.die()
robot2.die()
robot2.count_robots()
