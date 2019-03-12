# Help on class Constr in module gurobipy:

class Constr():
    """
    Constr(cmodel, rowno)

    Gurobi constraint object.  Constraints have a number of attributes.
    Some can be set (e.g., c.rhs = 0.0), while others can only be queried
    (e.g., print c.pi).  The most commonly used constraint attributes are:
      sense: Constraint sense ('<', '>', or '=').
      rhs: Right-hand side value.
      constrName: Constraint name.
      pi: Dual value in current solution
      slack: Slack in current solution.

    Type "help(GRB.attr)" for a list of all available attributes.

    Note that attribute modifications are handled in a lazy fashion.  You
    won't see the effect of a change until after the next call to Model.update()
    or Model.optimize().

    Methods defined here:

    __dir__(self)

    __getattr__(self, name)

    __init__(self, cmodel, rowno)

    __numrows__(self)

    __repr__(self)

    __rowno__(self)

    __setattr__(self, name, value)
    """

    def __init__(self, cmodel, rowno):
        pass


    def getAttr(self, attrname):
        """
        ROUTINE:
          getAttr(attrname)

        PURPOSE:
          Request the value of a constraint attribute.

        ARGUMENTS:
          attrname (string): The name of the requested attribute.

        RETURN VALUE:
          None.

        EXAMPLE:
          print constr.getAttr("constrName")

        NOTES:
          Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass


    def sameAs(self, other):
        """
        ROUTINE:
          sameAs(otherconstr)

        PURPOSE:
          Indicates whether two constraint objects refer to the same Gurobi model
          constraints.

        ARGUMENTS:
          otherconstr (Constr): The constraint to compare against.

        RETURN VALUE:
          True if both Constr objects refer to the same model constraint.

        EXAMPLE:
          constr1.sameAs(constr2)
        """
        pass


    def setAttr(self, attrname, newval):
        """
        ROUTINE:
          setAttr(attrname, newvalue)

        PURPOSE:
          Change the value of a constraint attribute.

        ARGUMENTS:
          attrname (string): The name of the attribute.
          newvalue: The desired new value.  The type of the value should be
                    compatible with the attribute type (e.g., an integer parameter
                    will take an integer value).

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          constr.setAttr("constrName", "New name")

        NOTES:
          Constraint attributes that can be set are:
            constrName: Constraint name.
            sense:      Constraint sense.
            rhs:        Right-hand side value.

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