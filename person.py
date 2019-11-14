# Joe Degere
# 11/13/19
# Person Homework


class Person:
    def __init__(self, first_name,last_name, weight, eye_color):
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight
        self.eyes = eye_color

    def description(self):
        print(f"My name is {self.first_name} {self.last_name}")
        print(f"I weigh in at about {self.weight}. Isn't that crazy!")
        print(f"I have a unique eye color, they're {self.eyes}")



