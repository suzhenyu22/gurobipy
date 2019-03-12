# Help on class Column in module gurobipy:

class Column():
    """
    Column(coeffs=None, constrs=None)

    Column class.  Columns consist of a set of coefficient, constraint
    pairs.  They capture the set of linear constraints in which a
    variable participates.

    The constructor for this class takes two arguments: Column(coeffs, constrs).
    The constrs argument gives a Constr or list of Constr.  The coeffs
    argument gives the corresponding coefficients
    (e.g., "col = Column([1.0, 2.0], [c0, c1])").

    Available methods on Column objects are:
      addTerms(coeffs, constrs): Add terms into a column.
      clear(): Set a column to zero.
      copy(): Copy a column.
      getCoeff(i): Return the coefficient for the term at index 'i'.
      getConstr(i): Return the constraint for the term at index 'i'.
      remove(i): Remove a term from the column.
      size(): Return the number of terms in the column.

    You can say "help(Column.method)" to get help on any method
    (e.g., help(Column.size)).

    Methods defined here:

    __init__(self, coeffs=None, constrs=None)

    __repr__(self)
    """

    def __init__(self,coeffs=None, constrs=None):
        pass


    def addTerms(self, coeffs, constrs):
        """
        ROUTINE:
          addTerms(coeffs, constrs)

        PURPOSE:
          Add a list of terms into a column.

        ARGUMENTS:
          coeffs (float or list of float): The coefficients for the new terms
          constrs (Constr or list of Constr): The constraints for the new terms

        EXAMPLE:
          c0.addTerms(1.0, x)
          c0.addTerms([1.0, 2.0], [x, y])
        """
        pass


    def clear(self):
        """
        ROUTINE:
          clear()

        PURPOSE:
          Clear a column.

        EXAMPLE:
          print c0.clear()
        """
        pass


    def copy(self):
        """
        ROUTINE:
          copy()

        PURPOSE:
          Copy a column.

        EXAMPLE:
          c1 = c0.copy()
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
          print c0.getCoeff(i)
        """
        pass


    def getConstr(self, i):
        """
        ROUTINE:
          getConstr(i)

        PURPOSE:
          Return the constraint for the term at index 'i'.

        ARGUMENTS:
          i (Int): Index of term whose constraint is requested

        RETURN VALUE:
          The requested constraint (a Constr object).

        EXAMPLE:
          print c0.getConstr(i)
        """
        pass


    def remove(self, which):
        """
        ROUTINE:
          remove(which)

        PURPOSE:
          Remove a term from the column.

        ARGUMENTS:
          which: Term to remove.  Can be an Int, in which case the term at
                 index 'which' is removed, or a Constr, in which case all terms
                 that involve the Constr 'which' are removed.

        EXAMPLE:
          print c0.remove(i)
        """
        pass


    def size(self):
        """
        ROUTINE:
          size()

        PURPOSE:
          Return the number of terms in a column.

        ARGUMENTS:
          None.

        RETURN VALUE:
          Number of terms in column.

        EXAMPLE:
          print c0.size()
        """
        pass

    # ----------------------------------------------------------------------
    # Data descriptors defined here:

    # __dict__
    # dictionary for instance variables (if defined)

    # __weakref__
    # list of weak references to the object (if defined)