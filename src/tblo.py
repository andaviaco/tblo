import numpy as np
import random as rand
import pprint as pp

from operator import attrgetter


class Learner(object):
    """docstring for Learner"""
    def __init__(self, initial_subjects, initial_fitness):
        super(Learner, self).__init__()

        self.subjects = initial_subjects
        self.fitness = initial_fitness

    def __repr__(self):
        return f'<Learner s: {self.subjects} | f: {self.fitness} >'


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
        # pp.pprint(self.learners)

        for i, learner in enumerate(self.learners):
            learner.subjects, learner.fitness = self.teacher_phase(learner, i)
            learner.subjects, learner.fitness = self.learner_phase(learner, i)

        # pp.pprint(self.learners)
        teacher = self.get_teacher()

        return teacher.subjects

    def initialize(self):
        self.learners = [self.create_learner() for i in range(self.npopulation)]

    def teacher_phase(self, learner, learner_index):
        teacher = self.get_teacher()
        tf = rand.randint(1, 2)
        c = np.zeros(len(teacher.subjects))

        for i, subject in enumerate(learner.subjects):
            s_mean = np.mean([s.subjects[i] for s in self.learners])
            r = rand.random()
            diff_mean = teacher.subjects[i] - (tf * s_mean)
            c[i] = subject + (r * diff_mean)

        rounded_c = np.around(c, decimals=4)

        best, best_fitness = self.select_best(learner.subjects, rounded_c)

        return (best, best_fitness)

    def learner_phase(self, learner, learner_index):
        k_index = self.random_learner_excluding([learner_index])
        k_learner = self.learners[k_index]
        k_subjets = k_learner.subjects
        c = np.zeros(len(learner.subjects))

        for i, subject in enumerate(learner.subjects):
            if learner.fitness < k_learner.fitness:
                diff = subject - k_subjets[i]
            else:
                diff = k_subjets[i] - subject

            r = rand.random()
            c[i] = subject + (r * diff)

        rounded_c = np.around(c, decimals=4)
        best, best_fitness = self.select_best(learner.subjects, rounded_c)

        return (best, best_fitness)

    def get_teacher(self):
        best = min(self.learners, key=attrgetter('fitness'))

        return best

    def select_best(self, subjects, c_subjects):
        s_fitness = self.fitness(subjects)
        c_fitness = self.fitness(c_subjects)

        if s_fitness > c_fitness:
            best = c_subjects
            best_fitness = c_fitness
        else:
            best = subjects
            best_fitness = s_fitness

        return (best, best_fitness)

    def random_learner_excluding(self, excluded_index):
        available_indexes = set(range(self.npopulation))
        exclude_set = set(excluded_index)
        diff = available_indexes - exclude_set
        selected = rand.choice(list(diff))

        return selected

    def fitness(self, solution):
        result = self.fn_eval(solution)

        if result >= 0:
            fitness = 1 / (1 + result)
        else:
            fitness = abs(result)

        return np.around(result, decimals=4)

    def create_learner(self):
        solution = self.random_vector(self.fn_lb, self.fn_ub)
        fitness = self.fitness(solution)

        return Learner(solution, fitness)

    def random_vector(self, lb, ub):
        r = rand.random()
        solution = lb + (ub - lb) * r

        return np.around(solution, decimals=4)
