# Help on class tuplelist in module gurobipy:

class tuplelist(list):
    """
    tuplelist(data=[], wild='*')

    Custom Gurobi class: tuplelist is a subclass of list that is
    designed to work with lists of tuples.  Using the select()
    method, this class allows you to efficiently select sub-lists of
    tuples by matching specific values in specific fields of the
    member tuples.

    For example:
      > l = tuplelist([(1, 2), (1, 3), (2, 3), (2, 4)])
      > print l.select('*', '*')
      [(1, 2), (1, 3), (2, 3), (2, 4)]
      > print l.select('*', 3)
      [(1, 3), (2, 3)]
      > print l.select(1, '*')
      [(1, 2), (1, 3)]

    Method resolution order:
        tuplelist
        builtins.list
        builtins.object

    Methods defined here:

    __add__(self, other)

    __contains__(self, val)
        ROUTINE:
          __contains__(val)

        PURPOSE:
          Determines if the specified value is contained in the tuplelist.
          This is faster than the parent method when calling "in" within
          a loop.

        ARGUMENTS:
          val: Value to match.

        RETURN VALUE:
          True if the values are in the list.

        EXAMPLE:
          if (1,2,3) in l

    __delitem__(self, i)

    __delslice__(self, i, j)

    __getslice__(self, b, c)

    __iadd__(self, other)



    __repr__(self)
    """


    def __init__(self, data=[], wild='*'):
        pass


    def append(self, x):
        pass


    def clean(self):
        """
        ROUTINE:
          clean()

        PURPOSE:
          The tuplelist class achieves it efficiency by building
          indices.  These indices are stored inside tuplelist
          objects, and they consume memory.  Call clean()
          if you wish to reclaim this memory.

        ARGUMENTS:
          None

        RETURN VALUE:
          None.

        EXAMPLE:
          l.clean()
        """
        pass


    def extend(self, L):
        pass


    def insert(self, i, x):
        pass


    def next(self, v):
        pass


    def nextc(self, v):
        pass


    def pop(self, i=-1):
        pass


    def prev(self, v):
        pass


    def prevc(self, v):
        pass


    def remove(self, x):
        pass


    def select(self, *vals):
        """
        ROUTINE:
          select(value1, value2, ...)

        PURPOSE:
          Selects a sub-list from a tuplelist.  All tuples that
          match the specified arguments in the corresponding fields
          are returned.  You can pass the string '*' (with the quotes)
          to indicate that any value is acceptable in the corresponding
          field.

        ARGUMENTS:
          value1: Value to match with first tuple member.
          value2: Value to match with second tuple member.
          ...

        RETURN VALUE:
          The matching sub-list.

        EXAMPLE:
          m = l.select('*', 1, '*', 'a')
        """
        pass

    # ----------------------------------------------------------------------
    # Data descriptors defined here:

    # __dict__
    # dictionary for instance variables (if defined)

    # __weakref__
    # list of weak references to the object (if defined)

    # ----------------------------------------------------------------------
    # Methods inherited from builtins.list:

    # __eq__(self, value, /)
    # Return self==value.

    # __ge__(self, value, /)
    # Return self>=value.

    # __getattribute__(self, name, /)
    # Return getattr(self, name).

    # __getitem__(...)
    # x.__getitem__(y) <==> x[y]

    # __gt__(self, value, /)
    # Return self>value.

    # __imul__(self, value, /)
    # Implement self*=value.

    # __iter__(self, /)
    # Implement iter(self).

    # __le__(self, value, /)
    # Return self<=value.

    # __len__(self, /)
    # Return len(self).

    # __lt__(self, value, /)
    # Return self<value.

    # __mul__(self, value, /)
    # Return self*value.

    # __ne__(self, value, /)
    # Return self!=value.

    # __reversed__(self, /)
    # Return a reverse iterator over the list.

    # __rmul__(self, value, /)
    # Return value*self.

    # __setitem__(self, key, value, /)
    # Set self[key] to value.

    # __sizeof__(self, /)
    # Return the size of the list in memory, in bytes.

    # clear(self, /)
    # Remove all items from list.

    # copy(self, /)
    # Return a shallow copy of the list.

    # count(self, value, /)
    # Return number of occurrences of value.

    # index(self, value, start=0, stop=9223372036854775807, /)
    # Return first index of value.

    # Raises ValueError if the value is not present.

    # reverse(self, /)
    # Reverse *IN PLACE*.

    # sort(self, /, *, key=None, reverse=False)
    # Stable sort *IN PLACE*.

    # ----------------------------------------------------------------------
    # Static methods inherited from builtins.list:

    # __new__(*args, **kwargs) from builtins.type
    # Create and return a new object.  See help(type) for accurate signature.

    # ----------------------------------------------------------------------
    # Data and other attributes inherited from builtins.list:

    # __hash__ = None
