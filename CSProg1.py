from __future__ import print_function
from ortools.linear_solver import pywraplp


def main():

    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('simple_lp_program',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Create the variables v1 and v2
    v1 = solver.NumVar(0, 1, 'v1')
    v2 = solver.NumVar(0, 2, 'v2')

    print("These are the number of the variables used = ", solver.NumVariables())

    # The constraint 0 <= x + y <= 2 which represents an equation
    ct = solver.Constraint(0, 2, 'ct')
    ct.SetCoefficient(v1, 1)
    ct.SetCoefficient(v2, 1)

    print('Number of constraints =', solver.NumConstraints())
  

    # Create the objective function, 3 * x + y.
    # This function needs to be maximized
    objective = solver.Objective()
    objective.SetCoefficient(v1, 3)
    objective.SetCoefficient(v1, 1)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())


if __name__ == '__main__':
    main()