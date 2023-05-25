#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ['mirage easy how to a split', 'pipebomb tutorial', 'scam vending machine', 'art of the respect', 'ap california', 'blood sacrifice']

    def log_in(self):
        pass

    def teach(self):
        one_piece_of_esoteric_knowledge_please = random.choice(self.knowledge)
        return one_piece_of_esoteric_knowledge_please