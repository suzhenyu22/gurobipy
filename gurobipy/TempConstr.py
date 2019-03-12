# Help on class TempConstr in module gurobipy:

class TempConstr():
    """
    TempConstr(lhs, sense, rhs)

    Gurobi temporary constraint object.  Objects of this class are created
    as intermediate results when building constraints using overloaded
    operators.

    Methods defined here:

    __ge__(self, rhs)

    __init__(self, lhs, sense, rhs)

    __le__(self, rhs)

    __repr__(self)

    __rshift__(self, other)

    ----------------------------------------------------------------------
    Data descriptors defined here:

    __dict__
        dictionary for instance variables (if defined)

    __weakref__
        list of weak references to the object (if defined)
    """

    def __init__(self, lhs, sense, rhs):
        pass