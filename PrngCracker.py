import functools
from utils import *


class PRNGCracker:

    def __init__(self):
        self.multiplier = None
        self.addends = None
        self.mod = None

    def find_parameters(self, states):
        self.find_mod(states)
        self.find_multiplier(states)
        self.find_addends(states)

    def all_parameters_are_filled(self):
        return self.multiplier and self.addends and self.mod

    def find_mod(self, states):
        diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
        zeroes = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
        self.mod = abs(functools.reduce(gcd, zeroes))

    def find_multiplier(self, states):
        self.multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], self.mod) % self.mod

    def find_addends(self, states):
        self.addends = (states[1] - states[0] * self.multiplier) % self.mod

    def run(self, previous_state):
        assert self.all_parameters_are_filled()
        return (self.multiplier * previous_state + self.addends) % self.mod
