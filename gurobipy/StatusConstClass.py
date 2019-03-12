# Help on class StatusConstClass in module gurobipy:

class StatusConstClass(object):
    """
    Gurobi optimization status codes (e.g., model.status == GRB.OPTIMAL):

      LOADED: Model loaded, but no solution information available
      OPTIMAL: Solve to optimality (subject to tolerances)
      INFEASIBLE: Model is infeasible
      INF_OR_UNBD: Model is either infeasible or unbounded
      UNBOUNDED: Model is unbounded
      CUTOFF: Objective is worse than specified cutoff value
      ITERATION_LIMIT: Optimization terminated due to iteration limit
      NODE_LIMIT: Optimization terminated due to node limit
      TIME_LIMIT: Optimization terminated due to time limit
      SOLUTION_LIMIT: Optimization terminated due to solution limit
      INTERRUPTED: User interrupted optimization
      NUMERIC: Optimization terminated due to numerical issues
      SUBOPTIMAL: Optimization terminated with a sub-optimal solution
      INPROGRESS: Optimization currently in progress
      USER_OBJ_LIMIT: Achieved user objective limit

    Methods defined here:

    __setattr__(self, name, value)

    ----------------------------------------------------------------------
    Data descriptors defined here:

    __dict__
        dictionary for instance variables (if defined)

    __weakref__
        list of weak references to the object (if defined)

    ----------------------------------------------------------------------
    Data and other attributes defined here:
    """

    CUTOFF = 6

    INFEASIBLE = 3

    INF_OR_UNBD = 4

    INPROGRESS = 14

    INTERRUPTED = 11

    ITERATION_LIMIT = 7

    LOADED = 1

    NODE_LIMIT = 8

    NUMERIC = 12

    OPTIMAL = 2

    SOLUTION_LIMIT = 10

    SUBOPTIMAL = 13

    TIME_LIMIT = 9

    UNBOUNDED = 5

    USER_OBJ_LIMIT = 15