# Help on class QConstr in module gurobipy:

class QConstr():
    """
    QConstr(cmodel, qconstrno)

    Gurobi quadratic constraint object.  Quadratic constraints have
    several attribute...

    Methods defined here:

    __dir__(self)

    __getattr__(self, name)

    __init__(self, cmodel, qconstrno)

    __qconstrno__(self)

    __repr__(self)

    __setattr__(self, name, value)
    """

    def __init__(self, cmodel, qconstrno):
        pass


    def getAttr(self, attrname):
        """
        ROUTINE:
          getAttr(attrname)

        PURPOSE:
          Request the value of a quadratic constraint attribute.

        ARGUMENTS:
          attrname (string): The name of the requested attribute.

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          print qc.getAttr("QCname")

        NOTES:
          Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass


    def setAttr(self, attrname, newval):
        """
        ROUTINE:
          setAttr(attrname, newvalue)

        PURPOSE:
          Change the value of a quadratic constraint attribute.

        ARGUMENTS:
          attrname (string): The name of the attribute.
          newvalue: The desired new value.  The type of the value should be
                    compatible with the attribute type (e.g., an integer parameter
                    will take an integer value).

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          qc.setAttr("QCname", "New name")

        NOTES:
          Constraint attributes that can be set are:
            QCname:  Constraint name.
            QCsense: Constraint sense.
            QCrhs:   Right-hand side value.

          Attributes changes are handled in a lazy fashion.  The effect of a
          change isn't visible until after the next call to Model.update() or
          Model.optimize().
        """
        pass

# ----------------------------------------------------------------------
# Data descriptors defined here:

# __dict__
# dictionary for instance variables (if defined)

# __weakref__
# list of weak references to the object (if defined)