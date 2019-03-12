# Help on class SOS in module gurobipy:

class SOS():
    """
    SOS(cmodel, sosno)

    Gurobi SOS object.  SOS objects have a single attribute: IISSOS.
    When an IIS is available, this attribute indicates whether the
    SOS object participates in the IIS.

    Methods defined here:

    __dir__(self)

    __getattr__(self, name)

    __init__(self, cmodel, sosno)

    __repr__(self)

    __sosno__(self)
    """


    def __init__(self, cmodel, sosno):
        pass


    def getAttr(self, attrname):
        """
        ROUTINE:
          getAttr(attrname)

        PURPOSE:
          Request the value of an SOS attribute.

        ARGUMENTS:
          attrname (string): The name of the requested attribute.

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          print sos.getAttr("IISSOS")

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
