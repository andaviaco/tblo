

class Learner(object):
    """docstring for Learner"""
    def __init__(self, initial_subjects, initial_fitness):
        super(Learner, self).__init__()

        self.subjects = initial_solution
        self.fitness = initial_fitness

    def __repr__(self):
        pass


class TBLO(object):
    def __init__(self, npopulation,  ngenerations, fn_eval, *, fn_lb, fn_ub):
        super(TBLO, self).__init__()

        self.npopulation = npopulation
        self.ngenerations = ngenerations
        self.fn_eval = fn_eval
        self.fn_lb = fn_lb
        self.fn_ub = fn_ub

    def optimize(self):
        pass

    def initialize(self):
        pass

    def teacher_phase(self):
        pass

    def learner_phase(self):
        pass

    def get_teacher(self):
        pass

    def create_learner(self):
        pass

    def random_learner_excluding(self, excluded_index):
        pass

    def random_vector(self, lb, ub):
        pass
