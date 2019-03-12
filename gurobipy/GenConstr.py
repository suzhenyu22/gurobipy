# Help on class GenConstr in module gurobipy:

class GenConstr():
    """
    GenConstr(cmodel, genconstrno)

    Gurobi GenConstr object.  GenConstr objects has two attributes:
    GenConstrType and IISGenConstr.
    The GenConstrType attribute indicates the type of the general constraint.
    When an IIS is available, the IISGenConstr attribute indicates whether the
    GenConstr object participates in the IIS.

    Methods defined here:

    __dir__(self)

    __genconstrno__(self)

    __getattr__(self, name)

    __init__(self, cmodel, genconstrno)

    __repr__(self)
    """

    def __init__(self, cmodel, genconstrno):
        pass

    def getAttr(self, attrname):
        """
        ROUTINE:
          getAttr(attrname)

        PURPOSE:
          Request the value of an GenConstr attribute.

        ARGUMENTS:
          attrname (string): The name of the requested attribute.

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          print genconstr.getAttr("IISGenConstr")

        NOTES:
          Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass

    # ----------------------------------------------------------------------
    # Data descriptors defined here:

    # __dict__
    # dictionary for instance variables (if defined)

    # __weakref__
    # list of weak references to the object (if defined)