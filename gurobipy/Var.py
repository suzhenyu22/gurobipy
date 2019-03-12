# Help on class Var in module gurobipy:

class Var():
    """
    Var(cmodel, colno)

    Gurobi variable object.  Variables have a number of attributes.
    Some can be set (e.g., v.ub = 0.0), while others can only be queried
    (e.g., print v.x). The most commonly used variable attributes are:
      obj: Linear objective coefficient.
      lb: Lower bound.
      ub: Upper bound.
      varName: Variable name.
      vType: Variable type ('C', 'B', 'I', 'S', or 'N').
      x: Solution value.
      rc: Solution reduced cost.
      xn: Solution value in an alternate MIP solution.

    Type "help(GRB.attr)" for a list of all available attributes.

    Note that attribute modifications are handled in a lazy fashion.  You
    won't see the effect of a change until after the next call to Model.update()
    or Model.optimize().

    Methods defined here:

    __add__(self, expr)

    __colno__(self)

    __dir__(self)

    __div__(self, constant)

    __eq__(self, rhs)

    __ge__(self, rhs)

    __getattr__(self, name)

    __hash__(self)

    __iadd__(self, expr)

    __imul__(self, expr)

    __init__(self, cmodel, colno)

    __isub__(self, expr)

    __le__(self, rhs)

    __mul__(self, expr)

    __ne__(self, rhs)

    __neg__(self)

    __numcols__(self)

    __radd__(self, expr)

    __repr__(self)

    __rmul__(self, expr)

    __rsub__(self, expr)

    __setattr__(self, name, value)

    __sub__(self, expr)

    __truediv__(self, constant)
    """

    def __init__(self, cmodel, colno):
        pass


    def getAttr(self, attrname):
        """
        ROUTINE:
          getAttr(attrname)

        PURPOSE:
          Request the value of a variable attribute.

        ARGUMENTS:
          attrname (string): The name of the requested attribute.

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          print var.getAttr("varName")

        NOTES:
          Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass


    def sameAs(self, other):
        """
        ROUTINE:
          sameAs(othervar)

        PURPOSE:
          Indicates whether two variable objects refer to the same Gurobi model
          variable.  You should use this instead of the '==' operator, since
          '==' is used to create linear constraints.

        ARGUMENTS:
          othervar (Var): The variable to compare against.

        RETURN VALUE:
          True if both Var objects refer to the same model variable.

        EXAMPLE:
          var1.sameAs(var2)
        """
        pass


    def setAttr(self, attrname, newval):
        """
        ROUTINE:
          setAttr(attrname, newvalue)

        PURPOSE:
          Change the value of a variable attribute.

        ARGUMENTS:
          attrname (string): The name of the attribute.
          newvalue: The desired new value.  The type of the value should be
                    compatible with the attribute type (e.g., an integer parameter
                    will take an integer value).

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          var.setAttr("varName", "New name")

        NOTES:
          Constraint attributes that can be set are:
            VarName:  Name of the variable.
            lb:       Lower bound.
            ub:       Upper bound.
            obj:      Objective coefficient.
            vType:    Variable type ('C', 'B', 'I', 'S', or 'N').

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