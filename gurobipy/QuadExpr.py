# Help on class QuadExpr in module gurobipy:

class QuadExpr():
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

    def __init__(self, *args, **kwargs):
        # Initialize self.  See help(type(self)) for accurate signature.
        pass


    def add(self, expr, mult=1.0):
        """
        ROUTINE:
          add(expr, mult=1.0)

        PURPOSE:
          Add a linear multiple of one expression into another.

        ARGUMENTS:
          expr (LinExpr or QuadExpr): The expression to add
          mult (float):               The linear multiplier

        EXAMPLE:
          expr1.add(expr2, 2.0)
        """
        pass


    def addConstant(self, constant):
        """
        ROUTINE:
          addConstant(constant)

        PURPOSE:
          Add a constant into a quadratic expression.

        ARGUMENTS:
          constant (float): The value to add

        EXAMPLE:
          expr.addConstant(3.5)
        """
        pass


    def addTerms(self, coeffs, vars, vars2=None):
        """
        ROUTINE:
          addTerms(coeffs, vars)
          addTerms(coeffs, vars, vars2)

        PURPOSE:
          Add a list of terms, either linear or quadratic, into a quadratic
          expression.

        ARGUMENTS:
          coeffs (list of float): The coefficients for the new terms
          vars (list of Var):     The variables for the new terms
          vars2 (list of Var):    The variables for the new terms

        EXAMPLE:
          expr.addTerms(1.0, x)
          expr.addTerms(1.0, x, x)
          expr.addTerms([1.0, 2.0], [x, y])
          expr.addTerms([1.0, 2.0], [x, y], [x, y])
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
          Copy a quadratic expression.

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


    def getLinExpr(self):
        """
        ROUTINE:
          getLinExpr()

        PURPOSE:
          Return the linear portion of a quadration expression (as a LinExpr
          object).

        ARGUMENTS:
          None.

        RETURN VALUE:
          Linear expression.

        EXAMPLE:
          print expr.getLinExpr()
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


    def getVar1(self):
        """
        ROUTINE:
          getVar1(i)

        PURPOSE:
          Return the first variable for the quadratic term at index 'i'.

        ARGUMENTS:
          i (Int): Index of quadratic term whose variable is requested

        RETURN VALUE:
          The requested variable.

        EXAMPLE:
          print expr.getVar1(i)
        """
        pass


    def getVar2(self, i):
        """
        ROUTINE:
          getVar2(i)

        PURPOSE:
          Return the second variable for the quadratic term at index 'i'.

        ARGUMENTS:
          i (Int): Index of quadratic term whose variable is requested

        RETURN VALUE:
          The requested variable.

        EXAMPLE:
          print expr.getVar2(i)
        """
        pass


    def remove(self, which):
        """
        ROUTINE:
          remove(which)

        PURPOSE:
          Remove a quadratic term from the expression.

        ARGUMENTS:
          which: Term to remove.  Can be an Int, in which case the quadratic term
                 at index 'which' is removed, or a Var, in which case all quadratic
                 terms that involve the Var 'which' are removed.

        EXAMPLE:
          print expr.remove(i)
        """
        pass


    def size(self):
        """
        ROUTINE:
          size()

        PURPOSE:
          Return the number of quadratic terms in a quadratic expression.

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