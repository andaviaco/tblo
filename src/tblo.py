import numpy as np
import random as rand
import pprint as pp


class Learner(object):
    """docstring for Learner"""
    def __init__(self, initial_subjects, initial_fitness):
        super(Learner, self).__init__()

        self.subjects = initial_subjects
        self.fitness = initial_fitness

    def __repr__(self):
        return f'<Learner s: {self.subjects} | f:{self.fitness} >'


class TBLO(object):
    learners = []

    def __init__(self, npopulation,  ngenerations, fn_eval, *, fn_lb, fn_ub):
        super(TBLO, self).__init__()

        self.npopulation = npopulation
        self.ngenerations = ngenerations
        self.fn_eval = fn_eval
        self.fn_lb = np.array(fn_lb)
        self.fn_ub = np.array(fn_ub)


    def optimize(self):
        self.initialize()
        pp.pprint(self.learners)

        return [None, None]

    def initialize(self):
        self.learners = [self.create_learner() for i in range(self.npopulation)]

    def teacher_phase(self):
        pass

    def learner_phase(self):
        pass

    def get_teacher(self):
        pass

    def random_learner_excluding(self, excluded_index):
        pass

    def fitness(self, solution):
        result = self.fn_eval(solution)

        return np.around(result, decimals=4)

    def create_learner(self):
        solution = self.random_vector(self.fn_lb, self.fn_ub)
        fitness = self.fitness(solution)

        return Learner(solution, fitness)

    def random_vector(self, lb, ub):
        r = rand.random()
        solution = lb + (ub - lb) * r

        return np.around(solution, decimals=4)
