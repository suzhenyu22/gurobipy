# Help on class LinExpr in module gurobipy:

class LinExpr():
    """
    Methods defined here:

    __add__(self, value, /)
        Return self+value.

    __eq__(self, value, /)
        Return self==value.

    __ge__(self, value, /)
        Return self>=value.

    __gt__(self, value, /)
        Return self>value.

    __iadd__(self, value, /)
        Return self+=value.

    __imul__(self, value, /)
        Return self*=value.

    __init__(self, /, *args, **kwargs)
        Initialize self.  See help(type(self)) for accurate signature.

    __isub__(self, value, /)
        Return self-=value.

    __le__(self, value, /)
        Return self<=value.

    __lt__(self, value, /)
        Return self<value.

    __mul__(self, value, /)
        Return self*value.

    __ne__(self, value, /)
        Return self!=value.

    __neg__(self, /)
        -self

    __radd__(self, value, /)
        Return value+self.

    __reduce__ = __reduce_cython__(...)

    __repr__(self, /)
        Return repr(self).

    __rmul__(self, value, /)
        Return value*self.

    __rsub__(self, value, /)
        Return value-self.

    __rtruediv__(self, value, /)
        Return value/self.

    __setstate__ = __setstate_cython__(...)

    __sub__(self, value, /)
        Return self-value.

    __truediv__(self, value, /)
        Return self/value.
    """

    def __init__(self):
        pass

    def add(self, expr, mult = 1.0):
        """
        ROUTINE:
          add(expr, mult=1.0)

        PURPOSE:
          Add a linear multiple of one expression into another.

        ARGUMENTS:
          expr (LinExpr): The expression to add
          mult (float):   The linear multiplier

        EXAMPLE:
          expr1.add(expr2, 2.0)
        """
        pass


    def addConstant(self, constant):
        """
        ROUTINE:
          addConstant(constant)

        PURPOSE:
          Add a constant into a linear expression.

        ARGUMENTS:
          constant (float): The value to add

        EXAMPLE:
          expr.addConstant(3.5)
        """
        pass


    def addTerms(self, coeffs, vars):
        """
        ROUTINE:
          addTerms(coeffs, vars)

        PURPOSE:
          Add a list of terms into a linear expression.

        ARGUMENTS:
          coeffs (list of float): The coefficients for the new terms
          vars (list of Var):     The variables for the new terms

        EXAMPLE:
          expr.addTerms(1.0, x)
          expr.addTerms([1.0, 2.0], [x, y])
        """
        pass


    def clear(self):
        """
        ROUTINE:
          clear()

        PURPOSE:
          Set a linear expression to zero.

        EXAMPLE:
          print expr.clear()
        """
        pass


    def copy(self):
        """
        ROUTINE:
          copy()

        PURPOSE:
          Copy a linear expression.

        EXAMPLE:
          expr2 = expr1.copy()
        """
        pass


    def getCoeff(self, i):
        """
        ROUTINE:
          getCoeff(i)

        PURPOSE:
          Return the coefficient for the term at index 'i'.

        ARGUMENTS:
          i (Int): Index of term whose coefficient is requested

        RETURN VALUE:
          The requested coefficient.

        EXAMPLE:
          print expr.getCoeff(i)
        """
        pass


    def getConstant(self):
        """
        ROUTINE:
          getConstant()

        PURPOSE:
          Return the constant terms from a linear expression.

        ARGUMENTS:
          None.

        RETURN VALUE:
          Constant for expression.

        EXAMPLE:
          print expr.getConstant()
        """
        pass


    def getValue(self):
        """
        ROUTINE:
          getValue()

        PURPOSE:
          Compute the value of the expression, using the current solution.

        ARGUMENTS:
          None.

        RETURN VALUE:
          The computed expression value.

        EXAMPLE:
          print model.getObjective().getValue()
        """
        pass


    def getVar(self, i):
        """
        ROUTINE:
          getVar(i)

        PURPOSE:
          Return the variable for the term at index 'i'.

        ARGUMENTS:
          i (Int): Index of term whose variable is requested

        RETURN VALUE:
          The requested variable (a Var object).

        EXAMPLE:
          print expr.getVar(i)
        """
        pass


    def remove(self, which):
        """
        ROUTINE:
          remove(which)

        PURPOSE:
          Remove a term from the expression.

        ARGUMENTS:
          which: Term to remove.  Can be an Int, in which case the term at
                 index 'which' is removed, or a Var, in which case all terms that
                 involve the Var 'which' are removed.

        EXAMPLE:
          print expr.remove(i)
        """
        pass


    def size(self):
        """
        ROUTINE:
          size()

        PURPOSE:
          Return the number of terms in a linear expression.

        ARGUMENTS:
          None.

        RETURN VALUE:
          Number of terms in expression.

        EXAMPLE:
          print expr.size()
        """
        pass

    # ----------------------------------------------------------------------
    # Static methods defined here:

    # __new__(*args, **kwargs) from builtins.type
    # Create and return a new object.  See help(type) for accurate signature.

    # ----------------------------------------------------------------------
    # Data and other attributes defined here:

    # __hash__ = None