from __future__ import print_function

from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count


def CPCrypto():
    """Solve the CP+IS+FUN==TRUE cryptarithm."""
    # Constraint programming engine
    model = cp_model.CpModel()

    base = 64

    C = model.NewIntVar(1, base - 1, 'C')
    R = model.NewIntVar(0, base - 1, 'R')
    Y = model.NewIntVar(1, base - 1, 'Y')
    P = model.NewIntVar(0, base - 1, 'P')
    T = model.NewIntVar(1, base - 1, 'T')
    O = model.NewIntVar(0, base - 1, 'O')
    P = model.NewIntVar(0, base - 1, 'P')
    Z = model.NewIntVar(1, base - 1, 'Z')
    L = model.NewIntVar(0, base - 1, 'L')
    E = model.NewIntVar(0, base - 1, 'E')

    # We need to group variables in a list to use the constraint AllDifferent.
    letters = [C, R, Y, P, T, O, P, Z, L, E]

    # Verify that we have enough digits.
    assert base >= len(letters)

    # Define constraints.
    model.AddAllDifferent(letters)

    # CP + IS + FUN = TRUE
    model.Add(C * base + R + Y * base + P + T * base * base + O * base +
              Y == T * base * base * base + Z * base * base + L * base + E)

    ### Solve model.
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(letters)
    status = solver.SearchForAllSolutions(model, solution_printer)

    print()
    print('Statistics')
    print('  - status          : %s' % solver.StatusName(status))
    print('  - conflicts       : %i' % solver.NumConflicts())
    print('  - branches        : %i' % solver.NumBranches())
    print('  - wall time       : %f s' % solver.WallTime())
    print('  - solutions found : %i' % solution_printer.solution_count())


if __name__ == '__main__':
    CPIsFunSat()