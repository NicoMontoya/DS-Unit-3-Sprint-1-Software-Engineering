#!/usr/bin/env python

import random

class Product:
    """Class represents everything that ACME sells

    Parameters
    -------------------------
    name: string
        string with no default
    price: int
        integer with default value 10
    weight: int
        integer with default value 20
    flammability: float
        float with default value 0.5
    identifier: int
        automatically genererated as a random (uniform) number 
        anywhere from 1000000 to 9999999, includisve)(inclusive).
    """
    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
            identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        calculates the price divided by the weight, and then returns a message: 
        if the ratio is less than 0.5 return "Not so stealable...", if it is 
        greater or equal to 0.5 but less than 1.0 return "Kinda stealable.", 
        and otherwise return "Very stealable!"
        """

        s_ability = self.price / self.weight 

        if s_ability < 0.5:
            return 'Not so stalable...'
        elif s_ability >= 0.5 and s_ability < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """
        calculates the flammability times the weight, and then returns a message: 
        if the product is less than 10 return "...fizzle.", if it is greater or 
        equal to 10 but less than 50 return "...boom!", and otherwise return 
        "...BABOOM!!"
        """

        explosiveness = self.flammability * self.weight

        if explosiveness < 10:
            return '...fizzle.'
        elif explosiveness >=10 and explosiveness < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

class BoxingGlove(Product):
    """
    Override certain parameters of the default Player class and add some
    functionality unique to BoxingGlove
    """
    def __init__(self, name=None, weight=10):
        super().__init__(name=name, weight=weight)

    def explode(self):
        """
        Overrides Product method to remind everyone that gloves don't explode
        """
        return '...It is a glove.'

    def punch(self):
        """
        returns "That tickles." if the weight is below 5, "Hey that hurt!" if 
        the weight is greater or equal to 5 but less than 15, and "OUCH!" 
        otherwise
        """

        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'

