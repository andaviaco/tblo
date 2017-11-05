import lib
from tblo import TBLO


def main():
    tblo_sphere = TBLO(500, 100, lib.sphere, fn_lb=[-5, -5], fn_ub=[5, 5])
    tblo_ackley = TBLO(500, 100, lib.ackley, fn_lb=[-20, -20], fn_ub=[20, 20])
    tblo_rastrigin = TBLO(500, 100, lib.rastrigin, fn_lb=[-5, -5], fn_ub=[5, 5])

    min_x, min_y = tblo_sphere.optimize()

    eval_result = lib.sphere([min_x, min_y])

    print(f'Sphere MIN: x={min_x}, y={min_y}')
    print(f'Sphere({min_x}, {min_y}) = {round(eval_result, 4)}')

    min_x, min_y = tblo_rastrigin.optimize()
    eval_result = lib.rastrigin([min_x, min_y])

    print(f'Rastrigin MIN: x={min_x}, y={min_y}')
    print(f'Rastrigin({min_x}, {min_y}) = {round(eval_result, 4)}')

    min_x, min_y = tblo_ackley.optimize()
    eval_result = lib.ackley([min_x, min_y])

    print(f'Ackley MIN: x={min_x}, y={min_y}')
    print(f'Ackley({min_x}, {min_y}) = {round(eval_result, 4)}')

if __name__ == '__main__':
    main()
